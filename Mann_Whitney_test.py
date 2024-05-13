import scipy.stats as stats
import os
import pandas as pd
directory_ney = "/content/drive/MyDrive/final_res/pr_ney"
flag = 0
directory_ins = "/content/drive/MyDrive/final_res/pr_ins"
results_of_exps_pr_ney = {}
results_of_exps_pr_ins = {}

directory = directory_ney
for filename in os.listdir(directory):
    if os.path.isdir(os.path.join(directory, filename)):
        for filename1 in os.listdir(os.path.join(directory, filename)):
            if os.path.isfile(os.path.join(os.path.join(directory, filename), filename1)):
                print(os.path.join(os.path.join(directory, filename), filename1))
                if filename1[-7:-4] == "ill":
                  df_ill = pd.read_csv(os.path.join(os.path.join(directory, filename), filename1), sep = '   ')
                  flag += 1
                else:
                  df_wel = pd.read_csv(os.path.join(os.path.join(directory, filename), filename1), sep = '   ')
                  flag += 1
                if flag == 2:
                  flag = 0
                  res_a = stats.mannwhitneyu(df_ill['a'], df_wel['a'])
                  res_v = stats.mannwhitneyu(df_ill['v'], df_wel['v'])
                  res_t0 = stats.mannwhitneyu(df_ill['t0'], df_wel['t0'])
                  res_st0 = stats.mannwhitneyu(df_ill['st0'], df_wel['st0'])
                  results_of_exps_pr_ney[filename1[:-7]] = [res_a, res_v, res_t0, res_st0]

directory = directory_ins
for filename in os.listdir(directory):
    if os.path.isdir(os.path.join(directory, filename)):
        for filename1 in os.listdir(os.path.join(directory, filename)):
            if os.path.isfile(os.path.join(os.path.join(directory, filename), filename1)):
                print(os.path.join(os.path.join(directory, filename), filename1))
                if filename1[-7:-4] == "ill":
                  df_ill = pd.read_csv(os.path.join(os.path.join(directory, filename), filename1), sep = '   ')
                  flag += 1
                else:
                  df_wel = pd.read_csv(os.path.join(os.path.join(directory, filename), filename1), sep = '   ')
                  flag += 1
                if flag == 2:
                  flag = 0
                  res_a = stats.mannwhitneyu(df_ill['a'], df_wel['a'])
                  res_v = stats.mannwhitneyu(df_ill['v'], df_wel['v'])
                  res_t0 = stats.mannwhitneyu(df_ill['t0'], df_wel['t0'])
                  res_st0 = stats.mannwhitneyu(df_ill['st0'], df_wel['st0'])
                  results_of_exps_pr_ins[filename1[:-7]] = [res_a, res_v, res_t0, res_st0]
