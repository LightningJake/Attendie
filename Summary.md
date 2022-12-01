### Transformers:

- Transformers support framework interoperability between PyTorch, TensorFlow.
- - ***Encoder*** - Task of the encoder, on the left half of the Transformer architecture, is to map an input sequence to a sequence of continuous representations, which is then fed into a decoder.
- ***Decoder*** - receives the output of the encoder together with the decoder output at the previous time step to generate an output sequence.
- ***BERT*** - ***Bidirectional Encoder Representations from Transformers***
model is really good at understanding language (and hence understanding input text) but less adequate at generating new text
- ***GPT*** - ***Generative Pre-trained Transformer*** 
is really good at generating text, but likely less good at BERT-like understanding simply because it utilizes the decoder segment of the vanilla Transformer.
- ***Pipelines*** - Objects that abstract most of the complex code from the library, offering a simple API dedicated to several tasks.
- ***Tokens*** - instance of a sequence of characters in some particular document that are grouped together as a useful semantic unit for processing.
- Based on shared subsequent tokens between produced sequence and the original document.
- Transformers provides APIs and tools to easily download and train state-of-the-art pretrained models. Using pretrained models.
