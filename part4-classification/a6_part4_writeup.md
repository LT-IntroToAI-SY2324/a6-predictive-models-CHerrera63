# Part 4 - Classification Writeup

After completing `a6_part4.py` answer the following questions

## Questions to answer

1. Comment out the StandardScaler and re-run your test. How accurate is the model? Why is that?
A: It is not as accurate as the standardized test (0.68 < 0.84), probably because without the scaling and the standardization, the mean and the varaibles aren't well placed and cause different numbers and results that decrease accuracy
2. How accurate is the model with the StandardScaler? Is this model accurate enough for the given use case? Explain.
It is pretty accurate with 0.84 accuracy. It should be accurate enough, because with everything organized it has created a model that can fit the data
3. Looking at the predicted and actual results, how did the model do? Was there a pattern to the inputs that the model was incorrect about?
A: Model did pretty good, very high accuracy. Things that could be incorrect about was the prediction that certain people would but the SUV when they actually wouldn't
4. Would a 34 year old Female who makes 56000 a year buy an SUV according to the model? Remember to scale the data before running it through the model.
A: Yes
