import pandas as pd
import numpy as np
import os

directory = "/content/drive/MyDrive/Special_folder/res_st/pr_ney"

for filename in os.listdir(directory):
    if os.path.isdir(os.path.join(directory, filename)):
        for filename1 in os.listdir(os.path.join(directory, filename)):
            if os.path.isfile(os.path.join(os.path.join(directory, filename), filename1)):
                if filename == "ColorStroop":
                    print(os.path.join(os.path.join(directory, filename), filename1))
                    df = pd.read_csv(os.path.join(os.path.join(directory, filename), filename1), sep = '\t')
                    df_zeroes = df.query('congr == 0.0')
                    df_ones = df.query('congr == 1.0')
                    df_res = df_zeroes[['response.corr', 'response.rt']]
                    df_res['response.corr'] = df_res['response.corr'].astype(int)
                    df_res.to_csv('/content/drive/MyDrive/Special_folder/res_st_1/pr_ney/ColorStroop/' + '00000' + filename1[:-4] + '.dat', sep='\t', index=False, header=False)
                    df_res = df_ones[['response.corr', 'response.rt']]
                    df_res['response.corr'] = df_res['response.corr'].astype(int)
                    df_res.to_csv('/content/drive/MyDrive/Special_folder/res_st_1/pr_ney/ColorStroop/' + '11111' + filename1[:-4] + '.dat', sep='\t', index=False, header=False)
                elif filename == "FlankerTask":
                    print(os.path.join(os.path.join(directory, filename), filename1))
                    df = pd.read_csv(os.path.join(os.path.join(directory, filename), filename1), sep = '\t')
                    df_zeroes = df.query('congruent == 0.0')
                    df_ones = df.query('congruent == 1.0')
                    vec_zeros = (df_zeroes['corrAns'] == df_zeroes['key_resp.keys']).astype(int)
                    df_zeroes['corr'] = vec_zeros
                    df_res = df_zeroes[['corr', 'key_resp.rt']]
                    df_res['corr'] = df_res['corr'].astype(int)
                    df_res.to_csv('/content/drive/MyDrive/Special_folder/res_st_1/pr_ney/FlankerTask/' + '00000' + filename1[:-4] + '.dat', sep='\t', index=False, header=False)
                    vec_ones = (df_ones['corrAns'] == df_ones['key_resp.keys']).astype(int)
                    df_ones['corr'] = vec_ones
                    df_res = df_ones[['corr', 'key_resp.rt']]
                    df_res['corr'] = df_res['corr'].astype(int)
                    df_res.to_csv('/content/drive/MyDrive/Special_folder/res_st_1/pr_ney/FlankerTask/' + '11111' + filename1[:-4] + '.dat', sep='\t', index=False, header=False)
                elif filename == "GoNoGo":
                    print(os.path.join(os.path.join(directory, filename), filename1))
                    df = pd.read_csv(os.path.join(os.path.join(directory, filename), filename1), sep = '\t')
                    df_res = df[['resp_trial_Test1.corr', 'resp_trial_Test1.rt']]
                    df_res['resp_trial_Test1.corr'] = df_res['resp_trial_Test1.corr'].astype(int)
                    df_res.to_csv('/content/drive/MyDrive/Special_folder/res_st_1/pr_ney/GoNoGo/' + filename1[:-4] + '.dat', sep='\t', index=False, header=False)
                elif filename == "NumericalStroop":
                    print(os.path.join(os.path.join(directory, filename), filename1))
                    df = pd.read_csv(os.path.join(os.path.join(directory, filename), filename1), sep = '\t')
                    df1 = df.query('task == "physical"')
                    df2 = df.query('task == "semantic"')
                    df_zeroes = df1.query('congruency ==  "cong"')
                    df_ones = df1.query('congruency == "neutral"')
                    df_twoes = df1.query('congruency == "incong"')
                    df_res = df_zeroes[['Response.corr', 'Response.rt']]
                    df_res['Response.corr'] = df_res['Response.corr'].astype(int)
                    df_res.to_csv('/content/drive/MyDrive/Special_folder/res_st_1/pr_ney/NumericalStroop/' + '00000phy' + filename1[:-4] + '.dat', sep='\t', index=False, header=False)
                    df_res = df_ones[['Response.corr', 'Response.rt']]
                    df_res['Response.corr'] = df_res['Response.corr'].astype(int)
                    df_res.to_csv('/content/drive/MyDrive/Special_folder/res_st_1/pr_ney/NumericalStroop/' + '11111phy' + filename1[:-4] + '.dat', sep='\t', index=False, header=False)
                    df_res = df_twoes[['Response.corr', 'Response.rt']]
                    df_res['Response.corr'] = df_res['Response.corr'].astype(int)
                    df_res.to_csv('/content/drive/MyDrive/Special_folder/res_st_1/pr_ney/NumericalStroop/' + '22222phy' + filename1[:-4] + '.dat', sep='\t', index=False, header=False)
                    df_zeroes2 = df2.query('congruency ==  "cong"')
                    df_ones2 = df2.query('congruency == "neutral"')
                    df_twoes2 = df2.query('congruency == "incong"')
                    df_res2 = df_zeroes2[['Response.corr', 'Response.rt']]
                    df_res2['Response.corr'] = df_res2['Response.corr'].astype(int)
                    df_res2.to_csv('/content/drive/MyDrive/Special_folder/res_st_1/pr_ney/NumericalStroop/' + '00000sem' + filename1[:-4] + '.dat', sep='\t', index=False, header=False)
                    df_res2 = df_ones2[['Response.corr', 'Response.rt']]
                    df_res2['Response.corr'] = df_res2['Response.corr'].astype(int)
                    df_res2.to_csv('/content/drive/MyDrive/Special_folder/res_st_1/pr_ney/NumericalStroop/' + '11111sem' + filename1[:-4] + '.dat', sep='\t', index=False, header=False)
                    df_res2 = df_twoes2[['Response.corr', 'Response.rt']]
                    df_res2['Response.corr'] = df_res2['Response.corr'].astype(int)
                    df_res2.to_csv('/content/drive/MyDrive/Special_folder/res_st_1/pr_ney/NumericalStroop/' + '22222sem' + filename1[:-4] + '.dat', sep='\t', index=False, header=False)
                elif filename == "N-back":
                    print(os.path.join(os.path.join(directory, filename), filename1))
                    df = pd.read_csv(os.path.join(os.path.join(directory, filename), filename1), sep = '\t')
                    df_res = df[['response.corr', 'response.rt']]
                    df_res['response.corr'] = df_res['response.corr'].astype(int)
                    df_res.to_csv('/content/drive/MyDrive/Special_folder/res_st_1/pr_ney/N-back/' + filename1[:-4] + '.dat', sep='\t', index=False, header=False)
                elif filename == "TaskSwitching":
                    print(os.path.join(os.path.join(directory, filename), filename1))
                    df = pd.read_csv(os.path.join(os.path.join(directory, filename), filename1), sep = '\t')
                    df['corr'] = df['corr'].astype(int)

                    df.to_csv('/content/drive/MyDrive/Special_folder/res_st_1/pr_ney/TaskSwitching/' + filename1[:-4] + '.dat', sep='\t', index=False, header=False)
