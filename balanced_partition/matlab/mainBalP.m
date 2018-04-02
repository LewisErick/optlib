% rules = [struct('actionID', 1, 'featureVec', [0.2]); struct('actionID',
% 2, 'featureVec', [0.3])];
% 
% featureIDS = [1]
% remaining = [4 5 6];
% capacity = 20
%
% You can only have two containers.
function [container1, container2] = mainBalP(rules, container1, featureIDs)
container2 = [];
[X] = getBalPFeatures(container1, container2, featureIDs);
while X(1) < 0.5 && size(container1, 2)
    actionID = getBestAction(X, rules);
    
    [container2, container1] = applyActionBalP(container2, container1, actionID);
    
    [X] = getBalPFeatures(container1, container2, featureIDs);
    
    container1 = container1
    container2 = container2
    
    "-----"
end
    
end