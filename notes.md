# Part 1
For the random selection, I used the python module `random`.
First, the function will open the `.gz`-archive in text mode and
store the lines in a list. Afterwards, I use the function `sample` from the
`random` module, to retrieve a number of random lines of
the stored list without duplications. The maximum possible number of samples will always
be the length of the list.

# Part 2
I tried to keep the representation of the samples as 
simple as possible. In the end, it is a list of 2-tuples, each representing 
a 5-gram. The first item of the tuple is a 4-tuple, representing
the endings of the surrounding words, the second part of the tuple
is a bit, showing, if the third word was a verb (the part of speech
can be easily switched by changing the `POS` constant in `mycode.py`)

# Part 6
**predictions for POS 'V'** 
```
SVM: linear kernel
_________________
Precision: 0.5106382978723404
Recall: 0.027972027972027972
F1 Score: 0.053038674033149165

SVM: rbf kernel
_________________
Precision: 0.7446808510638298
Recall: 0.020396270396270396
F1 Score: 0.03970504821327284
```

Both models perform surprisingly well, giving that it is only based on
the last two characters of the surrounding words. Especially, the rbf kernel
has a high precision. What is striking, that the recall is very low, compared
to the precision; there are still a lot of missing predictions for verbs. 

Interestingly, switching the POS from 'V' to 'N', increases the recall
by a lot. It is now even higher than the precision.
One reason for that may be the bigger number of positive samples 
in the training data. For verbs, there existed around 8000 to 9000 positive samples,
while there are around 30000 positive samples for nouns. 

**predictions for POS 'N'** 
```
SVM: linear kernel
_________________
Precision: 0.6597424684159378
Recall: 0.8730107699726732
F1 Score: 0.7515394727738186

SVM: rbf kernel
_________________
Precision: 0.6662198391420912
Recall: 0.8787976209612602
F1 Score: 0.7578845220766617
```


# Part Bonus
I used an MLP neural network to try another classification. The script can
just be called on the command line without any parameters:

```shell
python bonus.py
```
**predictions for POS 'V'** 
```
MLP
_________________
Precision: 0.28978388998035365
Recall: 0.16573033707865167
F1 Score: 0.21086490350250175
```

This classifier performs on verbs far worse than the SVM.
As the SVM, this model can predict the POS 'N' better and reaches a similar
performance as the SVM. 

**predictions for POS 'N'** 
```
MLP
_________________
Precision: 0.6904160574239
Recall: 0.8195014200063111
F1 Score: 0.7494408772815814
```

