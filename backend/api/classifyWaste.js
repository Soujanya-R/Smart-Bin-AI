function mockClassify(itemName) {
    const categories = ["Plastic","Paper","Organic","Metal","E-waste"];
    const category = categories[Math.floor(Math.random() * categories.length)];
    const confidence = (Math.random() * 0.3 + 0.7).toFixed(2); // 0.7-1.0
    return { category, confidence };
}

module.exports = { mockClassify };
