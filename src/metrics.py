from sklearn.model_selection import cross_validate

def multiple_scores(X,t,cv,*models):
    scoring = ['recall_macro', 'precision_micro', 'recall_micro', 'f1_macro','accuracy']
    all_scores  = []
    
    for model in models:
        all_scores.append(cross_validate(model,X,t,cv=cv,scoring=scoring))
        
    return all_scores






   


