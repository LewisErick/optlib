function actionID = getBestAction(featureVec, rules)
actionID = 1;
min_dist = 9999999;
for i=1:size(rules, 1)
    X = [featureVec; rules(i).featureVec];
    cand_dist = pdist(X,'euclidean');
    if cand_dist < min_dist
        actionID = rules(i).actionID;
        min_dist = cand_dist;
    end
end
end