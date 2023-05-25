// Input:

// [
//  (a, b) : a referred b
//  (b, c) : b referred c
//  (null, a): no one referred a, a is an organic hire
//  ('a', 'd')
//  ('a' 'e')
//  ('e', 'f')
//  ('e', 'g')
    // (null, 'y')
    // ('y', 'z')
// ]

// output: who has referred the most people both directly and indirectly
// a: 4
// b: 1
// e: 2
// 'a'


// 'a'         'y'
// /. \           \
// 'b'  'c'       'z' 

const assert = require('assert');


class Node {
  constructor (val) {
    this.val = val;
    this.root = false;
    this.children = [];
  }
  
  addChild (child) {
    this.children.push(child);
  }
}

function getSubtrees(node, hierachyOfReferrals) {
//   console.log(`node: ${JSON.stringify(node)}`);
  if (node.children){
    let count = 0;
    for (const child of node.children) {
        count += 1;
        console.log(`child: ${child}`);
        console.log(`hierachyOfReferrals: ${JSON.stringify(hierachyOfReferrals)}`);
        const childNode = hierachyOfReferrals.get(child);
        const subChildrenCount = getSubtrees(childNode);
        count += subChildrenCount;

    }
    return count;
  } else {
    return 1;
  }
}

function getPersonWithMostReferrals(input) {
    const hierachyOfReferrals = new Map();
    // hOfRef {'a': 'NodeA(val: 'a', children: [b, d, e], isRoot: true)', 'b': 'NodeB(val: 'b', children: [c], isRoot: false)', 'c', 'NodeC()'}
    
    for (const [referral, referred] of input) {
        if (referral === null) {
            if (!hierachyOfReferrals.has(referred)) {
                hierachyOfReferrals.set(referred, new Node(referred));
            }
            hierachyOfReferrals.get(referred).root = true;
        } else {
            if (hierachyOfReferrals.has(referral)) {
                // console.log(`ELSE 1 IF 2: adding ${referred} to ${referral}`)
                hierachyOfReferrals.get(referral).addChild(referred);
            } else {
                const referralNode = new Node(referral);
                // console.log(`ELSE 1 ELSE 2 adding ${referred} to ${referralNode.val}`)
                referralNode.addChild(referred);
                hierachyOfReferrals.set(referral, referralNode);
            }
        }
        if (!hierachyOfReferrals.has(referred)) {
            hierachyOfReferrals.set(referred, new Node(referred));
        }
        // console.log(`Referral: ${referral}`);
        // console.log(hierachyOfReferrals);
    }

    console.log(hierachyOfReferrals);
    let maxReferrals = [ null, 0];

    // for (const value in hierachyOfReferrals.values()) {
    //   console.log(hierachyOfReferrals);
    // //   if (node.root) {
    // //     // console.log(`person: ${person}`);
    // //     const childrenCount = getSubtrees(node, hierachyOfReferrals);
    // //     // console.log(`childrenCount: ${childrenCount}`);
    // //     if (childrenCount > maxReferrals[1]) {
    // //         maxReferrals = [person, childrenCount];
    // //     }
    // //   }
    // }

    const personWithMostReferals = maxReferrals[0];
    return personWithMostReferals;
}

const input = [
    ['a', 'b'],
    ['b', 'c'],
    [null, 'a'],
    ['a', 'd'],
    ['a', 'e'],
    ['e', 'f'],
    ['e', 'g'],
    [null, 'y'],
    ['y', 'z']
];

// console.log(getPersonWithMostReferrals(input));
// assert.equal(getPersonWithMostReferrals(input), 'a'); 
