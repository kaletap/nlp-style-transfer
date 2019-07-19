# Style transfer
## Goal: implement a tool changing style of a provided text.

## Sources:
* Style Transfer from Non-Parallel Text by
Cross-Alignment 
    * Paper: https://arxiv.org/pdf/1705.09655.pdf
    * Code: https://github.com/shentianxiao/language-style-transfer

* Adversarial Text Generation via
Feature-Mover’s Distance 
    * Paper: https://papers.nips.cc/paper/7717-adversarial-text-generation-via-feature-movers-distance.pdf
    * Code: https://github.com/shentianxiao/language-style-transfer [1]
    
## Progress:
1. Implemented data downloading (imdb) that will later be used for training. (17.07.19)
2. Changed code in language-style-transfer from python2 to python3. (17.07.19)
3. Found out how to run language-style-transfer code (python3.6 and tensorflow==1.3.0). Added casting to tf.int32 to 
fix a bug. (19.07.19)

## TODO:
1. Run this code (write requirements file / docker) on some corpora.
    
    
[1] Reimplementation of original code. Link to author's repository at http://zhegan27.github.io/Paper.html) was not 
available.

