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
Precision: 0.2
Recall: 0.0016825574873808188
F1 Score: 0.003337041156840934

SVM: rbf kernel
_________________
Precision: 0.0
Recall: 0.0
F1 Score: 0.0

```

While the linear model has some correct predictions, the rbf model, does
not predict any verbs in the third position at all. Therefore, all three 
measures are 0.
The linear model has some success. The precision of 12,5% is in my view
quiet high for only looking at the last two characters of the surrounding
words. Still, as seen in the recall score, there are still a lot of 
missing predictions for verbs. So the features seem not to be enough for the SVM
to safely predict the verb.

Interestingly, switching the POS from 'V' to 'N', increases the measures
by a lot. Furthermore, the recall score is also higher than the precision.
One reason for that may be the bigger number of positive samples 
in the training data

**predictions for POS 'N'** 
```
SVM: linear kernel
_________________
Precision: 0.6274014155712841
Recall: 0.9885295523339175
F1 Score: 0.7676130389064143

SVM: rbf kernel
_________________
Precision: 0.6362667803111016
Recall: 0.9514099091922893
F1 Score: 0.7625614505522569
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
Precision: 0.25
Recall: 0.004640371229698376
F1 Score: 0.00911161731207289
```

This classifier performs a lot better than the SVM.
As the SVM, this model can predict the POS 'N' also better. 

**predictions for POS 'N'** 
```
MLP
_________________
Precision: 0.6387798586968712
Recall: 0.9154612664738027
F1 Score: 0.752493559680296
```

