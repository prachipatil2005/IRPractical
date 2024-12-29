from sklearn.metrics import precision_score,recall_score,f1_score
ground_truth=[1,0,1,0,1,1,0,0,1,1]
predicted_relevance=[1,1,1,0,0,1,0,1,1,0]
precision=precision_score(ground_truth,predicted_relevance)
recall=recall_score(ground_truth,predicted_relevance)
f1=f1_score(ground_truth,predicted_relevance)
print("Precision: {:.2f}".format(precision))
print("Recall: {:.2f}".format(recall))
print("F1 score: {:.2f}".format(f1))