"""
清空编辑区内容，无需参数，无返回值
"""
delete_js = """
function removeAllChildrenUntilEmptyText(node) {
    while (node.firstChild) {
        const child = node.firstChild;

// 如果子节点的innerText不为空白字符，则移除子节点
        if (node.textContent.trim() !== '') {
            node.removeChild(child);
        } else {
// 如果子节点的innerText为空白字符，停止移除
            break;
        }
    }
}

const targetElement = document.querySelector('pre.editor__inner.markdown-highlighting'); // 替换为你要操作的标签的ID或其他选择器

if (targetElement) {
    removeAllChildrenUntilEmptyText(targetElement);
}
"""

# 执行粘贴事件
"""
需要content 作为参数，执行粘贴
"""
past_js = """
// 创建一个函数，用于模拟粘贴事件
function simulatePasteEvent(element, text) {
    // 创建一个自定义的粘贴事件
    data = new DataTransfer()
    data.setData("text/plain", text)
    const pasteEvent = new ClipboardEvent('paste', {
        clipboardData: data,
        bubbles: true,
        cancelable: true,
        composed: true,
    });
    pasteEvent.preventDefault()

    // 分发粘贴事件到指定元素
    element.dispatchEvent(pasteEvent);
}

let tag = document.querySelector('pre')
let text = arguments[0]
simulatePasteEvent(tag, text)
"""

open_tag_js = """
let addBtn = document.querySelector('button.tag__btn-tag')
let mouseEnterEvent = new MouseEvent('mouseenter', {
    bubbles: true,
    cancelable: true,
    view: window
});
addBtn.dispatchEvent(mouseEnterEvent)
"""

input_tag_js = """
const inputEvent = new Event('input', {
    bubbles: true, // 事件是否应该冒泡
    cancelable: true, // 事件是否可以被取消
});

function input2Tag(tag) {
    let inputTag = document.querySelector('div.mark_selection_box input')
    inputTag.value = tag
    inputTag.dispatchEvent(inputEvent)
    focusEvent = new Event("focus");
    inputTag.dispatchEvent(focusEvent)
}
input2Tag(arguments[0])
"""

select_tag_js = """
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


function executeSelect(tag) {
    let roles = document.querySelector('ul[role]').innerText.split('\\n')
    let index = findClosestMatch(tag, roles)
    document.querySelectorAll('ul[role] li')[index].click()
}
executeSelect(arguments[0])
"""
