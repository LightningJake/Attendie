The following points provide info about WhisperAI used in this project:-

- A Multilayer Perceptron (MLP) is a feedforward artificial neural network that generates a set of outputs from a set of inputs. An MLP is characterized by several layers of input nodes connected as a directed graph between the input and output layers. MLP uses backpropagation for training the network. MLP is a deep learning method.
- MLP is widely used for solving problems that require supervised learning as well as research into computational neuroscience and parallel distributed processing. Applications include speech recognition, image recognition, and machine translation
- The model is based on a regular encoder decoder transformer
- This model is way more robust than the other models available on the internet(Robust - strong and accurate)
- Whisper almost approaches human-level robustness and accuracy in terms of transcribing due to being trained in such a diverse set of data
- Stack of classic encoder and decoder blocks with the attention mechanism propagating information between both
- It will take the audio recording and split it into 30 seconds chunks and process them one by one
- For each 30 seconds chunks, it will encode the audio using the encoder section and save the position of each word said, and leverage the info to find what was said using the decoder
- the decoder will predict the tokens from all this info
- Tokens are basically the words being said…
- Then it will repeat the same process for the next word and use the same info as well as the info of the previous word which would help to guess the next word
- This model is trained with more than almost 600,000 hours of multilingual and multitasking supervised data collected from the web.
