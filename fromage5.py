import spacy
import numpy as np
from collections import Counter
nlp = spacy.load("en_core_web_lg")

text = "Andrew feels great!"
"""""
"Andrew considers him a fool." --> 2 nsubj and ccomp
"Andrew likes cake." --> 1 nsubj and dobj
"Andrew feels great!"
"""
doc = nlp(text)
sentence_list = list(doc.sents)
sent_text_list = []
sent_dep_list = []
for sentence in sentence_list:

    word_dep_list = []
    word_text_list = []
    for item in sentence:
        word_dep_list.append(item.dep_)
        word_text_list.append(item.text)
    print('text list -- >', word_text_list)
    print('dep list -->', word_dep_list)
    sent_text_list.append(word_text_list)
    sent_dep_list.append(word_dep_list)
    print()


print()
'subect->ROOT->object'
i = 0
for sentence in sent_dep_list:
    #First identify the duplicate dependency
    duplicate_counter = Counter(sentence)
    print(duplicate_counter)
    duplicate_dep = list([item for item in duplicate_counter if duplicate_counter[item] > 1])
    print(duplicate_dep,'duplicate dependency')

    if len(duplicate_dep) > 0:
        print('There is a duplicate')
        duplicate_dep = duplicate_dep[0]
        print(duplicate_dep, '--> duplicate dependency')
        #Find leading and lagging
        for x in sentence:
            if x == duplicate_dep:
                print(sentence.index(x))
                leading_nsubj_idx = sentence.index(x)
                break

        for y in reversed(range(0, len(sentence))):
            print(y, sentence[y])
            if sentence[y] == duplicate_dep:
                print(y)
                lagging_nsubj_idx = y
                break
        #Identify the leading index as the start of subject clause and the lagging index as start of compound clause


    else:
        print('There is no duplicate')
        if 'nsubj' in sentence:
            subject_index = sentence.index('nsubj')
            print('nsubj at index-->', subject_index)

    if 'ROOT' in sentence:
        root_index = sentence.index('ROOT')
        print('ROOT at index-->', root_index)

    if 'dobj' in sentence and len(duplicate_dep) == 0:
        dobj_index = sentence.index('dobj')
        print('dobj at index-->', dobj_index)
    if 'pobj' in sentence and len(duplicate_dep) == 0:
        pobj_index = sentence.index('pobj')
        print('pobj at index-->', pobj_index)
    if 'xcomp' in sentence and len(duplicate_dep) == 0:
        xcomp_index = sentence.index('xcomp')
        print('xcomp at index-->', xcomp_index)
    if 'acomp' in sentence and len(duplicate_dep) == 0:
        acomp_index = sentence.index('acomp')
        print('acomp at index-->', acomp_index)

    textual_list = sent_text_list[i]
    print(textual_list, '<--- text list sentence at index', i)
    print()
    # First find the root clause using the root index
    root_clause = textual_list[root_index]
    if len(duplicate_dep) == 0:
        #Now we find the rest of the clauses using the indices with non-duplicate dependencies
        if ('dobj_index' or 'pobj_index') in locals() and 'xcomp_index' not in locals():
            print('There are dependency objects')

            if subject_index < root_index < (dobj_index or pobj_index):
                subject_clause = textual_list[:root_index]
                root_clause = textual_list[root_index]
                object_clause = textual_list[root_index + 1:]
                print(subject_clause, 'is the subject at the index', i)

            elif (dobj_index or pobj_index) < root_index < subject_index:
                object_clause = textual_list[:root_index]
                root_clause = textual_list[root_index]
                subject_clause = textual_list[root_index + 1:]

        if ('dobj_index' or 'pobj_index') not in locals() and 'xcomp_index' in locals():
            print('There are no dependency objects')

            if subject_index < root_index < xcomp_index:
                subject_clause = textual_list[:root_index]
                root_clause = textual_list[root_index]
                xcomp_clause = textual_list[root_index + 1:]

            elif xcomp_index < root_index < subject_index:
                xcomp_clause = textual_list[:root_index]
                root_clause = textual_list[root_index]
                subject_clause = textual_list[root_index + 1:]

        if ('dobj_index' or 'pobj_index') not in locals() and 'acomp_index' in locals():
            print('There are no dependency objects')

            if subject_index < root_index < acomp_index:
                subject_clause = textual_list[:root_index]
                root_clause = textual_list[root_index]
                acomp_clause = textual_list[root_index + 1:]

            elif acomp_index < root_index < subject_index:
                acomp_clause = textual_list[:root_index]
                root_clause = textual_list[root_index]
                subject_clause = textual_list[root_index + 1:]

    if len(duplicate_dep) > 0:
        subject_clause = textual_list[:root_index]
        root_clause = textual_list[root_index]
        compound_clause = textual_list[root_index + 1:]

    #Now we must print out the clauses
    price_argument = nlp('price')

    if len(duplicate_dep) == 0:
        if 'subject_clause' in locals():
            subject_clause = ' '.join(subject_clause)
            subject_clause = str(subject_clause)
            print(subject_clause, '<====== subject clause')
            del subject_clause
        if 'root_clause' in locals():
            print(root_clause, '<===== root')
            del root_clause
        if 'object_clause' in locals():
            object_clause = ' '.join(object_clause)
            object_clause = str(object_clause)
            print(object_clause, '<====== object clause')
            del object_clause
        if 'xcomp_clause' in locals():
            xcomp_clause = ' '.join(xcomp_clause)
            xcomp_clause = str(xcomp_clause)
            print(xcomp_clause, '<======= xcomp clause')
            del xcomp_clause
        if 'acomp_clause' in locals():
            acomp_clause = ' '.join(acomp_clause)
            acomp_clause = str(acomp_clause)
            print(acomp_clause, '<======= acomp clause')
            del acomp_clause

    if len(duplicate_dep) > 0:
        if 'subject_clause' in locals():
            subject_clause = ' '.join(subject_clause)
            subject_clause = str(subject_clause)
            print(subject_clause, '<====== subject clause')
            del subject_clause
        if 'root_clause' in locals():
            print(root_clause, '<===== root')
            del root_clause
        if 'compound_clause' in locals():
            compound_clause = ' '.join(compound_clause)
            compound_clause = str(compound_clause)
            print(compound_clause, '<===== compound clause')
            del compound_clause






