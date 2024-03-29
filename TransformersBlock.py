import numpy as np

def dropout(x, dropout_rate=0.1):
    # A simplified version of dropout; in practice, use frameworks like TensorFlow or PyTorch
    keep_rate = 1 - dropout_rate
    mask = np.random.binomial(1, keep_rate, size=x.shape)
    return x * mask / keep_rate

def softmax(x, axis=-1):
    x_exp = np.exp(x - np.max(x, axis=axis, keepdims=True))
    return x_exp / np.sum(x_exp, axis=axis, keepdims=True)

def scaled_dot_product_attention(Q, K, V, mask=None):
    matmul_qk = np.matmul(Q, K.swapaxes(-1, -2))
    d_k = Q.shape[-1]
    scaled_attention_logits = matmul_qk / np.sqrt(d_k)
    
    if mask is not None:
        scaled_attention_logits += (mask * -1e9)
    
    attention_weights = softmax(scaled_attention_logits, axis=-1)
    output = np.matmul(attention_weights, V)
    return output

def split_heads(x, num_heads):
    batch_size, seq_length, d_model = x.shape
    depth = d_model // num_heads
    x = x.reshape(batch_size, seq_length, num_heads, depth)
    return x.swapaxes(1, 2)

def multi_head_attention(Q, K, V, num_heads, mask=None):
    d_model = Q.shape[-1]
    Q = split_heads(Q, num_heads)
    K = split_heads(K, num_heads)
    V = split_heads(V, num_heads)
    
    scaled_attention = scaled_dot_product_attention(Q, K, V, mask)
    scaled_attention = scaled_attention.swapaxes(1, 2)
    
    concat_attention = scaled_attention.reshape(scaled_attention.shape[0], -1, d_model)
    return concat_attention

def position_wise_feed_forward_network(d_model, d_ff):
    return np.random.randn(d_model, d_ff), np.random.randn(d_ff), np.random.randn(d_ff, d_model), np.random.randn(d_model)

def feed_forward(x, weights):
    W1, b1, W2, b2 = weights
    x = np.dot(x, W1) + b1
    x = np.maximum(0, x)  # ReLU
    x = np.dot(x, W2) + b2
    return x

def positional_encoding(position, d_model):
    angle_rads = np.arange(position)[:, np.newaxis] / np.power(10000, (2 * (np.arange(d_model)[np.newaxis, :] // 2)) / np.float32(d_model))
    angle_rads[:, 0::2] = np.sin(angle_rads[:, 0::2])
    angle_rads[:, 1::2] = np.cos(angle_rads[:, 1::2])
    pos_encoding = angle_rads[np.newaxis, ...]
    return pos_encoding

def layer_norm(x, epsilon=1e-6):
    mean = np.mean(x, axis=-1, keepdims=True)
    var = np.var(x, axis=-1, keepdims=True)
    return (x - mean) / np.sqrt(var + epsilon)

def transformer_block(x, num_heads, d_ff, dropout_rate=0.1, mask=None):
    attn_output = multi_head_attention(x, x, x, num_heads, mask)
    attn_output = dropout(attn_output, dropout_rate)
    x = layer_norm(x + attn_output)
    ff_weights = position_wise_feed_forward_network(x.shape[-1], d_ff)
    ff_output = feed_forward(x, ff_weights)
    ff_output = dropout(ff_output, dropout_rate)
    output = layer_norm(x + ff_output)
    return output

# Example usage
seq_length = 10
d_model = 512
num_heads = 8
d_ff = 2048
batch_size = 1

x = np.random.rand(batch_size, seq_length, d_model)
mask = np.zeros((batch_size, seq_length, seq_length))
pos_encoding = positional_encoding(seq_length, d_model)
x += pos_encoding
transformed_x = transformer_block(x, num_heads, d_ff, mask=mask)
print(transformed_x.shape)