

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-06 17:51:24
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-06 17:51:31
 * @Description:
 * @TODO::
 * @Reference:https://github.com/drcat101/wids-datathon-2020/blob/master/wids_datathon_catboost.ipynb
-->
def preprocess(csvfile):
    df = pd.read_csv(csvfile)
    labels = df['hospital_death'].tolist()
    df = df.fillna(-999)
    df = df.drop(['encounter_id', 'patient_id', 'hospital_death', 'readmission_status'], axis=1)
    return df, labels
