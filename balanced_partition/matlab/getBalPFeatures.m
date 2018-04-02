% 1. Balance entre los dos contenedores
function [featureVec] = getBalPFeatures(container1, container2, featureIDs)
featureVec = zeros(1, length(featureIDs));
for i = 1:length(featureIDs)
    if featureIDs(i) == 1
        featureVec(i) = sum(container2) / (sum(container1) + sum(container2));
    end
end
end