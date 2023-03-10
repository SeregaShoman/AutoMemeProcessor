import random
import tensorflow as tf

def generate_msg_txt(model):
    states = None
    next_char = tf.constant(['\n'])
    result = [next_char]
    for n in range(200):
        next_char, states = model.generate_one_step(next_char, states=states)
        result.append(next_char)
    generated_text = tf.strings.join(result)[0].numpy().decode("utf-8")
    text_list = generated_text.split('\n')[2:-2]
    random_text = random.choice(text_list)
    return random_text