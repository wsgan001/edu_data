import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# data1 = pd.read_csv('../data/Run 1/big-data-1_enrolments.csv',usecols=[0])
# data2 = pd.read_csv('../data/Run 1/big-data-1_step-activity.csv')
#
# data1 = pd.read_csv('../data/Run 2/big-data-2_enrolments.csv',usecols=[0])
# data2 = pd.read_csv('../data/Run 2/big-data-2_step-activity.csv')
#
# data1 = pd.read_csv('../data/Run 3/big-data-3_enrolments.csv',usecols=[0])
# data2 = pd.read_csv('../data/Run 3/big-data-3_step-activity.csv')
#
# data1 = pd.read_csv('../data/Run 5/the-mind-is-flat-5_enrolments.csv',usecols=[0])
# data2 = pd.read_csv('../data/Run 5/the-mind-is-flat-5_step-activity.csv')
#
# data1 = pd.read_csv('../data/Run 6/the-mind-is-flat-6_enrolments.csv',usecols=[0])
# data2 = pd.read_csv('../data/Run 6/the-mind-is-flat-6_step-activity.csv')
#
data1 = pd.read_csv('../data/Run 7/the-mind-is-flat-7_enrolments.csv',usecols=[0])
data2 = pd.read_csv('../data/Run 7/the-mind-is-flat-7_step-activity.csv')

#Joiners
joiners = data1[data1.learner_id != ''].count()
print(joiners)

#learners
grouped = data2.groupby('learner_id')
learners = grouped.size()
print(learners)

#Active Learners
ActiveLearners = data2[data2['last_completed_at'].notnull()].groupby('learner_id').size()
print(ActiveLearners)

#Returning Learners
ReturningLearners = data2[(data2['last_completed_at'].notnull()) & (data2['week_number'] != 1)].groupby('learner_id').size()
print(ReturningLearners)

#Fully Participating Learners
FullyParticipatingLearner = data2[data2['last_completed_at'].notnull()].groupby(['week_number','step_number']).describe()
FullyParticipatingLearner.to_csv('../data/ReturningLearners.csv', index=False, encoding='utf-8')
# 按照week_number step_number聚合分组之后102条记录 learner_id出现102次即全部参与课程
temp = data2.groupby('learner_id').describe()
temp.to_csv('../data/temp.csv', index=False, encoding='utf-8')
read_temp = pd.read_csv('../data/temp.csv',skiprows=[0])
FullyParticipatingLearners = read_temp[read_temp['count'] == 102.0].count()
print(FullyParticipatingLearners)

#s=pd.DataFrame([joiners,learners,ActiveLearners,ReturningLearners,FullyParticipatingLearners],index=['joiners','learners','ActiveLearners','ReturningLearners','FullyParticipatingLearners'])
s=pd.DataFrame([16385,7751,5821,3312,480],index=['joiners','learners','ActiveLearners','ReturningLearners','FullyParticipatingLearners'])
s.plot(kind='bar')
plt.xticks(np.arange(5),('joiners','learners','ActiveLearners','ReturningLearners','FullyParticipatingLearners'),rotation=27)
plt.xlabel('label')
plt.ylabel('')
plt.show()
















