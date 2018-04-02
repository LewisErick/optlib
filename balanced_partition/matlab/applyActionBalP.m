% 1. Max
% 2. Min
function [container2, container1] = applyActionBalP(container2, container1, actionID)
if actionID == 1
    [M, I] = max(container1);
    container1(I) = [];
    container2 = [container2 M];
elseif actionID == 2
    [M, I] = min(container1);
    container1(I) = [];
    container2 = [container2 M];
end
end