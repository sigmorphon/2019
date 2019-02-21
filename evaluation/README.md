Evaluation
---

The official evaluation scripts live in this directory. We have provided sample output so you can see how it should be run, as well as demonstrating the intended output format.

Each task's evaluation script requires both the reference file (with gold annotations/inflections) and the model's guesses.

```bash
$ python3 evaluate_2019_task1.py \
>     --reference sample_2019_task1_gold.txt \
>     --output sample_2019_task1_output.txt
# acccuracy:	75.00	levenshtein:	1.62
python3 evaluate_2019_task2.py \
>     --reference sample_2019_task2_gold.txt
>     --output sample_2019_task2_output.txt
# INFO:evaluate_2019_task2:Lemma acc, Lemma Levenshtein, morph acc, morph F1
# 80.00	0.53	93.33	98.70

```
