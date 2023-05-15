// 121. Best Time to Buy and Sell Stock
// SOLVED? Yes

// Say you have an array for which the ith element is the price of a given stock on day i.

// If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

// Note that you cannot sell a stock before you buy one.

// Example 1:

// Input: [7,1,5,3,6,4]
// Output: 5
// Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
//              Not 7-1 = 6, as selling price needs to be larger than buying price.
// Example 2:

// Input: [7,6,4,3,1]
// Output: 0
// Explanation: In this case, no transaction is done, i.e. max profit = 0.

const maxProfit = prices => {
	let maxProfit = 0;
	let buyPrice;
	let sellPrice;

	for (const i in prices){
		sellPrice = prices[i];
		if (i >= 1) {
			maxProfit = Math.max(maxProfit, sellPrice - buyPrice);
			buyPrice = Math.min(buyPrice, prices[i]);
		} else {
			buyPrice = prices[i];
		}
	}

	return maxProfit;
};

console.log(maxProfit([7,1,5,3,6,4]));


// NOT AS PRETTY AS ABOVE, BUT WORKS

/**
 * @param {number[]} prices
 * @return {number}
 */

var maxProfit = function(prices) {

    let maxProfit = 0;
    let minBuyPrice = 100000;

    // We first sell on dayTwoPrice
    for (let dayTwo = 1; dayTwo < prices.length; dayTwo++ ){

        let newBuyPrice = prices[dayTwo - 1]; 
        let newSellPrice = prices[dayTwo]; 

        // Need to ensure that newSellPrice & maxSellPrice is AFTER minBuyPrice and newBuyPrice
        minBuyPrice = Math.min(minBuyPrice, newBuyPrice); 


        const newProfit = newSellPrice - minBuyPrice; 
        maxProfit = Math.max(maxProfit, newProfit);
    }

    return maxProfit;
    
};
