[nltk 词性标注 tag 列表](https://blog.csdn.net/weixin_43720526/article/details/120548774)

> 了解  tag 列表是为了区分哪些是实词 哪些是虚词

`实词`是指实在意义，能独立承担句子成分的词，包括名词、代词、形容词、副词、动词、数词。而且，实词有词性的变化。

1. 名词 (n.)：表示人、事物、地点或抽象概念的名称。如：boy, morning, bag, etc.
2. 代词 (pron.)：主要用来代替名词。如：who, she, you, it, etc.
3. 形容词 (adj.)：表示人或事物的性质和特征。如：good, right, white, etc.
4. 数词 (num.)：表示数目或事物的顺序。如：one, two, first, second, etc.
5. 动词 (v.)：表示动作或状态。如：am, is, have, see, etc.
6. 副词 (adv.)：修饰动词、形容词、副词，说明时间、地点、程度等。如：now, very, here, often, etc.

`虚词`没有实在意义，不能独立承担句子成分，包括冠词、介词、连词、感叹词。而且，虚词没有词性的变化。

1. 冠词 (art..)：用在名词前，帮助说明名词。如：a, an, the.
2. 介词 (prep.)：表示它后面的名词或代词与其他句子成分的关系。如：in, on, from, etc.
3. 连词 (conj.)：用来连接词、短语或句子。如：and, but, before, etc.
4. 感叹词 (interj..)：表示喜、怒、哀、乐等情感。如：on, well, hi, hello, etc.

因此据此可以得出非实词的标签有：CC 、DT、IN、PDT、RP、TO、UH

| 标签 |                 原词                  | 含义                     | 举例                                                  |
| :--- | :-----------------------------------: | :----------------------- | ----------------------------------------------------- |
| CC   |        coordinatingconjunction        | 连词                     | and, or,but, if, while,although                       |
| CD   |             cardinaldigit             | 数词                     | twenty-four, fourth, 1991,14:24                       |
| DT   |              determiner               | 限定词                   | the, a, some, most,every, no                          |
| EX   |           existentialthere            | 存在量词                 | there, there’s                                        |
| FW   |              foreignword              | 外来词                   | dolce, ersatz, esprit, quo,maitre                     |
| IN   | preposition/subordinating conjunction | 介词连词                 | on, of,at, with,by,into, under                        |
| JJ   |               adjective               | 形容词                   | new,good, high, special, big, local                   |
| JJR  |         adjective comparative         | 形容词比较级             | bleaker braver breezier briefer brighter brisker      |
| JJS  |        adjective, superlative         | 形容词最高级             | calmest cheapest choicest classiest cleanest clearest |
| LS   |              listmarker               | 标记                     |                                                       |
| MD   |                 modal                 | 情态动词                 | can cannot could couldn’t                             |
| NN   |            noun , singular            | 名词                     | year,home, costs, time, education                     |
| NNS  |              nounplural               | 名词复数                 | undergraduates scotches                               |
| NNP  |         propernoun, singular          | 专有名词                 | Alison,Africa,April,Washington                        |
| NNPS |          proper noun, plural          | 专有名词复数             | Americans Americas Amharas Amityvilles                |
| PDT  |             predeterminer             | 前限定词                 | all both half many                                    |
| POS  |           possessiveending            | 所有格标记 ’             | 's                                                    |
| PRP  |            personalpronoun            | 人称代词                 |                                                       |
| PRP$ |          possessive pronoun           | 所有格                   | her his mine my our ours                              |
| RB   |                adverb                 | 副词                     | occasionally unabatingly maddeningly                  |
| RBR  |          adverb,comparative           | 副词比较级               | further gloomier grander                              |
| RBS  |          adverb,superlative           | 副词最高级               | best biggest bluntest earliest                        |
| RP   |               particle                | 虚词                     | aboard about across along apart                       |
| SYM  |                 符号                  | % & ’ ‘’ ‘’. ) )         |                                                       |
| TO   |                  to                   | 词 to                    | to                                                    |
| UH   |             interjection              | 感叹词                   | Goodbye Goody Gosh Wow                                |
| VB   |            verb, baseform             | 动词                     | ask assemble assess                                   |
| VBD  |            verb, pasttense            | 动词过去式               | dipped pleaded swiped                                 |
| VBG  |    verb,gerund/present participle     | 动词现在分词             | telegraphing stirring focusing                        |
| VBN  |         verb, pastparticiple          | 动词过去分词             | multihulled dilapidated aerosolized                   |
| VBP  |      verb,sing. present, non-3d       | 动词现在式非第三人称时态 | predominate wrap resort sue                           |
| VBZ  |     verb, 3rdperson sing. present     | 动词现在式第三人称时态   | bases reconstructs marks                              |
| WDT  |           wh-determiner Wh            | 限定词                   | who,which,when,what,where,how                         |
| WP   |              wh-pronoun               | WH代词                   | that what whatever                                    |
| WP$  |         possessivewh-pronoun          | WH代词所有格             | whose                                                 |
| WRB  |               wh-abverb               | WH 副词                  | -                                                     |



> 中文词性标注 tag
>
> ·实词再细分为名词、动词、形容词、数词、量词、代词以及特殊实词拟声词、叹词；
>
> ·虚词再细分为副词、介词、连词、助词、叹词和拟声词六类
>
> 因此基于 pyltp 进行词性标注是虚词的标签有：c、d、e、g、h、i、o、u、wp

![image-20230206155853299](E:\杂七杂八的东西\typeorm 图片存储区\image-20230206155853299.png)
