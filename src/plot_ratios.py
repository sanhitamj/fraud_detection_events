# ratio_list = []
# thresholds = range(2, 2000)
# feature = "body_length"

def list_ratios(feature, thresholds):
    """
    For plotting a comparison of the fraud/nonfraud ratio of 
    a particular feature at various thresholds
    """
    for threshold in thresholds:

        df['comparison'] = df[feature] < cutoff_length


        fraud_short = float((df[df['fraud'] == True]['comparison'] == True).sum())\
                       / float((df[df['fraud'] == True]['comparison'] == False).count())

        premium_short = float((df[df['fraud'] == False]['comparison'] == True).sum()) \
                        / (df[df['fraud'] == False]['comparison'] == False).count()

        ratio = fraud_short / premium_short
        ratio_list.append(ratio)




# plt.figure(figsize=(10, 7))
# plt.subplot(111)
# plt.plot(cutoffs, fraud_short_list, 'b--')
# ax = plt.gca()
# ax.set_xlim([0, 250])
# plt.title("Description Lengths")
# plt.ylabel("Fraud Shorts / Non-Fraud Shorts")
# plt.xlabel("Shortness Cutoff")
#
# plt.savefig("../images/cutoff.png")
#
