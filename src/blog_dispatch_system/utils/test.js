function calculateLevenshteinDistance(s1, s2) {
    // 创建一个二维数组来存储编辑距离
    const distanceMatrix = Array.from(Array(s1.length + 1), () => Array(s2.length + 1).fill(0));

    // 初始化第一行和第一列
    for (let i = 0; i <= s1.length; i++) {
        distanceMatrix[i][0] = i;
    }

    for (let j = 0; j <= s2.length; j++) {
        distanceMatrix[0][j] = j;
    }

    // 填充编辑距离矩阵
    for (let i = 1; i <= s1.length; i++) {
        for (let j = 1; j <= s2.length; j++) {
            const cost = s1[i - 1] === s2[j - 1] ? 0 : 1;
            distanceMatrix[i][j] = Math.min(
                distanceMatrix[i - 1][j] + 1, // 删除操作
                distanceMatrix[i][j - 1] + 1, // 插入操作
                distanceMatrix[i - 1][j - 1] + cost // 替换操作
            );
        }
    }

    // 返回编辑距离
    return distanceMatrix[s1.length][s2.length];
}

function findClosestMatch(originalLabel, candidateLabels) {
    let minDistance = Number.MAX_SAFE_INTEGER;
    let closestIndex = -1;

    for (let i = 0; i < candidateLabels.length; i++) {
        const distance = calculateLevenshteinDistance(originalLabel, candidateLabels[i]);
        if (distance < minDistance) {
            minDistance = distance;
            closestIndex = i;
        }
    }

    return closestIndex;
}



let tags = arguments[0]




