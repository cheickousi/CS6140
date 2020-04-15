import sqlite3

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def getMisraGries(Data, k_1):
    counter_m = 0
    Labels = np.empty(shape=k_1, dtype=np.dtype('U25'))
    Counters = np.zeros(shape=k_1)
    for each_character in Data:
        if Labels.__contains__(each_character):
            index = np.argwhere(Labels == each_character)
            Counters[index[0][0]] += 1
        else:
            if Counters.__contains__(0):
                empty_index = np.where(Counters == 0)[0][0]
                Labels[empty_index] = each_character
                Counters[empty_index] = 1
            else:
                Counters -= 1
        counter_m += 1
    return Counters, Labels, (Counters / counter_m) * 100


def getSingleWordInjury(bagWords, wordString):
    if wordString.__contains__("/"):
        ListWord = wordString.split("/")
        first_two_words = ListWord[0].split(" ")
        firstWord = first_two_words[0]
        next_two_words = ListWord[1].split(" ")
        next_firstWord = next_two_words[0]
        bagWords.append(firstWord.strip().title())
        bagWords.append(next_firstWord.strip().title())
    else:
        if len(" ".join(wordString.strip().split(" ")[:2]).strip()) == 1:
            bagWords.append(" ".join(wordString.strip().split(" ")[:2]).title())
        else:
            first_two_words = " ".join(wordString.strip().split(" ")[:2]).strip().split(" ")
            if len(first_two_words) > 0:
                firstWord = first_two_words[0]
                if firstWord.__contains__('back') or firstWord.__contains__('respiratory'):
                    if len(first_two_words) == 2:
                        bagWords.append(first_two_words[1].strip().title())
                if len(firstWord.strip()) > 0:
                    bagWords.append(firstWord.strip().title())
    return bagWords


def getTwoWordsInjury(bagWords, wordString):
    if wordString.__contains__("/"):
        ListWord = wordString.split("/")
        first_two_words = ListWord[0]
        next_two_words = ListWord[1]
        bagWords.append(first_two_words.strip())
        bagWords.append(next_two_words.strip())
    else:
        first_two_words = " ".join(wordString.split(" ")[:2])
        if len(first_two_words.strip()) > 0:
            bagWords.append(first_two_words.strip())
    return bagWords


def create_connection(db_file):
    """ create a database connection to the SQLite database
           specified by db_file
       :param db_file: database file
       :return: Connection object or None
       """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)

    return conn


directory = "/Users/CheickSissoko/Documents/SQLite/"
local_filename = "/Users/CheickSissoko/Documents/Spring2020_CS6140/groupproject/first_draft_injuries.csv"

conn = create_connection('/Users/CheickSissoko/Documents/SQLite/nba_injuries.db3')

sql = 'SELECT TYPE_OF_INJURY_CLEANSED as words FROM INJURY_DATA2 where TYPE_OF_INJURY_CLEANSED is not null'

injuryBagWords = pd.read_sql(sql=sql, con=conn)
bagWords = []
for idx, each_row in injuryBagWords.iterrows():
    wordString = str(each_row.loc['words']).strip()
    if wordString.__contains__("injury"):
        wordString = wordString.strip().replace(" ", "_")
    if wordString.__contains__("in"):
        wordString = wordString.replace(' in ', '')
    if wordString.__contains__("partially"):
        wordString = wordString.replace('partially ', '')
    if wordString.__contains__("(P)"):
        wordString = wordString.replace('(P) ', '')
        wordString = wordString.replace('(P)', '')
    if wordString.__contains__("(CBC)"):
        wordString = wordString.replace('(CBC)', '')
        if wordString.__contains__("left"):
            wordString = wordString.replace(' left ', '')
    bagWords = getSingleWordInjury(bagWords, wordString)
    bagWords = getTwoWordsInjury(bagWords, wordString)

k = 400
labels, counters, counter_ration = getMisraGries(bagWords, k)
rlabels = pd.DataFrame(labels, columns=['Counter'])
rCounters = pd.DataFrame(counters, columns=['Label'])
rRatio = pd.DataFrame(counter_ration, columns=['Counter_ratio'])
rep = pd.concat([rlabels, rCounters, rRatio], axis=1)

final_report = rep[rep['Counter_ratio'] > 1].sort_values(by=['Counter_ratio'])
final_report = final_report[final_report['Label'] != ""]
final_report = final_report[final_report['Label'] != "Back"]
print(final_report.sort_values(by='Counter_ratio', ascending=False))

fig, ax = plt.subplots(figsize=(10, 5))
ax.barh(final_report["Label"], final_report["Counter_ratio"])
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')
ax.set(xlabel='Ratio/Percentage', ylabel='Injury Type',
       title='Misra Gries Most frequent Injuries')

# fig = plt.figure()
# plt.scatter(final_report['Label'], final_report['Counter'], s=final_report['Counter_ratio'] * 10, alpha=.5,
#             edgecolors="red",
#             c="white", zorder=2)
# plot grid behind markers
# plt.grid(ls="--", zorder=1)
# take care of long labels
# fig.autofmt_xdate()
# plt.tight_layout()
# plt.show()

# create padding column from values for circles that are neither too small nor too large
final_report["padd"] = 0.5 * (final_report['Counter'] - final_report.Counter.min()) / (
        final_report.Counter.max() - final_report.Counter.min()) + 0.5
fig = plt.figure()
# prepare the axes for the plot - you can also order your categories at this step
s = plt.scatter(sorted(final_report.Label.unique()), sorted(final_report.Label.unique(), reverse=True), s=0)
# plot data row-wise as text with circle radius according to Count
for row in final_report.itertuples():
    bbox_props = dict(boxstyle="circle, pad = {}".format(row.padd), fc="w", ec="b", lw=2)
    plt.annotate(str(np.round(row.Counter_ratio, 0)) + "%", xy=(row.Label, row.Label), bbox=bbox_props, ha="center",
                 va="center", zorder=2,
                 clip_on=True)

# plot grid behind markers
plt.grid(ls="--", zorder=1)
# take care of long labels
fig.autofmt_xdate()
plt.tight_layout()
plt.title("Misra Gries - Ratio")
plt.show()
