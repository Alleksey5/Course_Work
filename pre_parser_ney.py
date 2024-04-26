import pandas as pd
import numpy as np
import os

directory = "/content/drive/MyDrive/Special_folder/Для студентов/Проект_нейроонко"

for filename in os.listdir(directory):
    if os.path.isdir(os.path.join(directory, filename)):
        for filename1 in os.listdir(os.path.join(directory, filename)):
            if os.path.isfile(os.path.join(os.path.join(directory, filename), filename1)):
                if filename == "ColorStroop":
                    print(os.path.join(os.path.join(directory, filename), filename1))
                    df = pd.read_csv(os.path.join(os.path.join(directory, filename), filename1))

                    if 'feedback.started' in df.columns:
                        fname = 'feedback.started'
                    else:
                        fname = 'feedback_image.started'

                    df_filtered = df[(df[fname].isna()) & (df['response.rt'] > 0.150)]
                    arr = df_filtered['response.rt']

                    arr_new = np.log(arr)

                    Sample_average = np.mean(arr_new)

                    Var = np.sqrt(np.mean((arr_new - Sample_average) ** 2))


                    def func(x):
                        return (np.log(x) - Sample_average) / Var


                    df_f = df_filtered[df_filtered['response.rt'].apply(func) < 3]
                    df_f1 = df_f[df_f['response.rt'].apply(func) > -3]
                    df_res = df_f1[['word', 'cor', 'dir', 'congr', 'response.keys', 'response.corr', 'response.rt']]
                    df_res.to_csv('/content/drive/MyDrive/Special_folder/res_st/pr_ney/ColorStroop/' + filename1[:-4] + '.dat', sep='\t', index=False)
                elif filename == "FlankerTask":
                    print(os.path.join(os.path.join(directory, filename), filename1))
                    df = pd.read_csv(os.path.join(os.path.join(directory, filename), filename1))

                    df_filtered = df[(df['key_resp.rt'] > 0.150)]
                    arr = df_filtered['key_resp.rt']

                    arr_new = np.log(arr)

                    Sample_average = np.mean(arr_new)

                    Var = np.sqrt(np.mean((arr_new - Sample_average) ** 2))


                    def func(x):
                        return (np.log(x) - Sample_average) / Var


                    df_f = df_filtered[df_filtered['key_resp.rt'].apply(func) < 3]
                    df_f1 = df_f[df_f['key_resp.rt'].apply(func) > -3]
                    df_res = df_f1[['input', 'congruent', 'corrAns', 'key_resp.keys', 'key_resp.rt']]
                    df_res.to_csv('/content/drive/MyDrive/Special_folder/res_st/pr_ney/FlankerTask/' + filename1[:-4] + '.dat', sep='\t', index=False)
                elif filename == "GoNoGo":
                    print(os.path.join(os.path.join(directory, filename), filename1))
                    df = pd.read_csv(os.path.join(os.path.join(directory, filename), filename1))

                    df_filtered = df[(df['resp_trial_Test1.rt'] > 0.150)]
                    arr = df_filtered['resp_trial_Test1.rt']

                    arr_new = np.log(arr)

                    Sample_average = np.mean(arr_new)

                    Var = np.sqrt(np.mean((arr_new - Sample_average) ** 2))


                    def func(x):
                        return (np.log(x) - Sample_average) / Var


                    df_f = df_filtered[df_filtered['resp_trial_Test1.rt'].apply(func) < 3]
                    df_f1 = df_f[df_f['resp_trial_Test1.rt'].apply(func) > -3]
                    df_res = df_f1[['stimulus_test1', 'corrAns_test1', 'resp_trial_Test1.keys', 'resp_trial_Test1.corr', 'resp_trial_Test1.rt']]
                    df_res.to_csv('/content/drive/MyDrive/Special_folder/res_st/pr_ney/GoNoGo/' + filename1[:-4] + '.dat', sep='\t', index=False)
                elif filename == "NumericalStroop":
                    print(os.path.join(os.path.join(directory, filename), filename1))
                    df = pd.read_csv(os.path.join(os.path.join(directory, filename), filename1))

                    df_filtered = df[(df['ftrials.thisRepN'].isna()) & (df['Response.rt'] > 0.150)]
                    arr = df_filtered['Response.rt']

                    arr_new = np.log(arr)

                    Sample_average = np.mean(arr_new)

                    Var = np.sqrt(np.mean((arr_new - Sample_average) ** 2))


                    def func(x):
                        return (np.log(x) - Sample_average) / Var


                    df_f = df_filtered[df_filtered['Response.rt'].apply(func) < 3]
                    df_f1 = df_f[df_f['Response.rt'].apply(func) > -3]
                    df_res = df_f1[['task', 'size1', 'size2', 'number1', 'number2', 'corrAns', 'congruency', 'distance', 'Response.keys', 'Response.corr', 'Response.rt']]
                    df_res.to_csv('/content/drive/MyDrive/Special_folder/res_st/pr_ney/NumericalStroop/' + filename1[:-4] + '.dat', sep='\t', index=False)
                elif filename == "N-back":
                    print(os.path.join(os.path.join(directory, filename), filename1))
                    df = pd.read_csv(os.path.join(os.path.join(directory, filename), filename1))

                    df_filtered = df[(df['response.rt'] > 0.150)]
                    arr = df_filtered['response.rt']

                    arr_new = np.log(arr)

                    Sample_average = np.mean(arr_new)

                    Var = np.sqrt(np.mean((arr_new - Sample_average) ** 2))


                    def func(x):
                        return (np.log(x) - Sample_average) / Var


                    df_f = df_filtered[df_filtered['response.rt'].apply(func) < 3]
                    df_f1 = df_f[df_f['response.rt'].apply(func) > -3]
                    df_res = df_f1[['square', 'location', 'corrAns', 'response.keys', 'response.corr', 'response.rt']]
                    df_res.to_csv('/content/drive/MyDrive/Special_folder/res_st/pr_ney/N-back/' + filename1[:-4] + '.dat', sep='\t', index=False)
                elif filename == "TaskSwitching":
                    print(os.path.join(os.path.join(directory, filename), filename1))
                    dfq = pd.read_csv(os.path.join(os.path.join(directory, filename), filename1))
                    df = dfq.fillna(0)

                    df_filtered = df[(df['shape_resp.rt'] > 0.15) | (df['key_resp_33.rt'] > 0.150) | (df['key_resp_34.rt'] > 0.150) | (df['key_resp_35.rt'] > 0.150)]
                    arr1 = df_filtered['shape_resp.rt']
                    arr2 = df_filtered['key_resp_33.rt']
                    arr3 = df_filtered['key_resp_34.rt']
                    arr4 = df_filtered['key_resp_35.rt']
                    arr = arr1 + arr2 + arr3 + arr4

                    arr_new = np.log(arr)

                    Sample_average = np.mean(arr_new)
                    Var = np.sqrt(np.mean((arr_new - Sample_average) ** 2))

                    def func(x):
                      return (np.log(x) - Sample_average) / Var

                    df_f = df_filtered[df_filtered['shape_resp.rt'].apply(func) < 3]
                    df_f1 = df_f[df_f['shape_resp.rt'].apply(func) > -3]
                    df_f2 = df_filtered[df_filtered['key_resp_33.rt'].apply(func) < 3]
                    df_f3 = df_f2[df_f2['key_resp_33.rt'].apply(func) > -3]
                    df_f4 = df_filtered[df_filtered['key_resp_34.rt'].apply(func) < 3]
                    df_f5 = df_f4[df_f4['key_resp_34.rt'].apply(func) > -3]
                    df_f6 = df_filtered[df_filtered['key_resp_35.rt'].apply(func) < 3]
                    df_f7 = df_f6[df_f6['key_resp_35.rt'].apply(func) > -3]
                    df_w = pd.concat([df_f1, df_f3, df_f5, df_f7], ignore_index=True)
                    df_w_1 = df_w.query('SwitchTrial == "repeat"')
                    df_w_2 = df_w.query('SwitchTrial == "switch"')
                    vec_sh_rt_1 = df_w_1['shape_resp.rt']
                    vec_sh_cor_1 = df_w_1['shape_resp.corr']
                    vec_k33_rt_1 = df_w_1['key_resp_33.rt']
                    vec_k33_cor_1 = df_w_1['key_resp_33.corr']
                    vec_k34_rt_1 = df_w_1['key_resp_34.rt']
                    vec_k34_cor_1 = df_w_1['key_resp_34.corr']
                    vec_k35_rt_1 = df_w_1['key_resp_35.rt']
                    vec_k35_cor_1 = df_w_1['key_resp_35.corr']
                    res_vec_rt_1 = vec_sh_rt_1 + vec_k33_rt_1 + vec_k34_rt_1 + vec_k35_rt_1
                    res_vec_corr_1 = vec_sh_cor_1 + vec_k33_cor_1 + vec_k34_cor_1 + vec_k35_cor_1
                    data = {
                        'corr' : res_vec_corr_1,
                        'rt' : res_vec_rt_1
                    }
                    dffin = pd.DataFrame(data)
                    dffin.to_csv('/content/drive/MyDrive/Special_folder/res_st/pr_ney/TaskSwitching/' + 'rep' + filename1[:-4] + '.dat', sep='\t', index=False)
                    vec_sh_rt_2 = df_w_2['shape_resp.rt']
                    vec_sh_cor_2 = df_w_2['shape_resp.corr']
                    vec_k33_rt_2 = df_w_2['key_resp_33.rt']
                    vec_k33_cor_2 = df_w_2['key_resp_33.corr']
                    vec_k34_rt_2 = df_w_2['key_resp_34.rt']
                    vec_k34_cor_2 = df_w_2['key_resp_34.corr']
                    vec_k35_rt_2 = df_w_2['key_resp_35.rt']
                    vec_k35_cor_2 = df_w_2['key_resp_35.corr']
                    res_vec_rt_2 = vec_sh_rt_2 + vec_k33_rt_2 + vec_k34_rt_2 + vec_k35_rt_2
                    res_vec_corr_2 = vec_sh_cor_2 + vec_k33_cor_2 + vec_k34_cor_2 + vec_k35_cor_2
                    data_2 = {
                        'corr' : res_vec_corr_2,
                        'rt' : res_vec_rt_2
                    }
                    dffin = pd.DataFrame(data_2)
                    dffin.to_csv('/content/drive/MyDrive/Special_folder/res_st/pr_ney/TaskSwitching/' + 'switch' + filename1[:-4] + '.dat', sep='\t', index=False)
