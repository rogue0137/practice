// Given this kind of input:
// [{
//   id: number,
//   parent_id: number || None,
//   name: string,
// }, ...]

// where
//   `name` is the name of a place
//   `id` is a number unique to the list
//   `parent_id` is one of the `id`s indicating that this place lies within the geographical boundaries of the parent

// Example JSON data also pasted here: 

const input = [
  {
    "name": "Bay Area",
    "id": 1,
    "parent_id": 99
  },
  {
    "name": "California",
    "id": 99,
    "parent_id": null
  }
  ,
  {
    "name": "Oakland",
    "id": 2,
    "parent_id": 1
  },
    {
    "name": "Nextdoor NOPA",
    "id": 3,
    "parent_id": 6
  },
  {
    "name": "San Francisco",
    "id": 6,
    "parent_id": 8
  },
  {
    "name": "San Francisco County",
    "id": 8,
    "parent_id": 1
  }
  ,
  {
    "name": "New York City",
    "id": 4,
    "parent_id": null
  },
  {
    "name": "Brooklyn",
    "id": 9,
    "parent_id": 4
  },
  {
    "name": "Queens",
    "id": 5,
    "parent_id": 4
  }
]

// Produce this kind of output:
// California
// -Bay Area
// --Oakland
// --San Francisco County
// ---San Francisco
// ----Nextdoor NOPA
// New York City
// -Brooklyn
// -Queens

// function orderCitiesAndStates(citiesAndStates) {
    
//     const citiesAndStatesLength = citiesAndStates.length;
    
//     const family = {};
//     const parents = []
    
    
//     // build family using parents
//     for (let i = 0; i < citiesAndStatesLength; i++){
//         let cityOrState = citiesAndStates[i];
        
//         let name = cityOrState['name']; 
//         let id = cityOrState['id']; 
//         let parentId = cityOrState['parent_id']; 
        
//         family[id] = {
//             name,
//             id,
//             parentId,
//             children: []
//         }
        
//     }
//     console.log('FIRST COMPUTED FAMILY');
//     console.log(family);
    
//     // build family by adding children
//     for (let i = 0; i < citiesAndStatesLength; i++){
//         let cityOrState = citiesAndStates[i]; 
        
//         let id = cityOrState['id']; 
//         let parentId = cityOrState['parent_id']; 
        
//         if (parentId === null) {
//             console.log('parent id: ', id);
//             parents.push([id]);
//         }
        
//         if (parentId in family ){
//             family[parentId].children.push(id); 
            
//         }        
//     }
//     console.log('UPDATED FAMILY');
//     console.log(family);
//     console.log('PARENTS');
//     console.log(parents);
    
//     for (const parent in parents) {
//         const children = parents[parent]?.children;
//         if (children) {
//             parents[i+1] = children;
//         }

//     }
//     for (let i = 0; i < parents.length; i++){
//         const currentParent = parents[i];
//         const children = family[currentParent]?.children;
//     }

//     console.log('UPDATED PARENTS');
//     console.log(parents);
// }


function getAnswerUsingFind(input) {
    const family = {};
    
    input.forEach(location => {
      family[location.id] = { name: location.name, children: [] };
    });
    
    for (const id in family) {
      // search through the input to find a location with the same id
      // then access it's parent_id 
      const parentId = input.find(location => location.id === Number(id)).parent_id;
      // if the parent_id is not null, add the id to the parent's children array
      if (parentId !== null) {
        family[parentId].children.push(family[id]);
      }
    }
    
    // Traverse the object hierarchy to print the output in the required format
    // this function implements a depth-first search algorithm. 
    // Specifically, it performs a pre-order traversal of the tree, 
    // where each node is visited before its children are visited.
    function printHierarchy(node, prefix = 0) {
      const dashes = '-'.repeat(prefix);
      console.log(dashes + node.name); // Visits the node BEFORE it's children
      node.children.forEach((child) => {
        printHierarchy(child, prefix + 1); // recursively visits it's children
      });
    }
    
    for (const id in family) {
      if (input.find(location => location.id === Number(id)).parent_id === null) {
        printHierarchy(family[id]);
      }
    }

}

function getAnswerUsingForLoops(input) {

    const family = {};

    for (const location of input ) {
        // long version
        // const id = location.id;
        // const name = location.name;
        // const parentId = location.parent_id;
        // family[id] = { name, children: [] };

        // short version
        family[location.id] = { name: location.name, parentId: location.parent_id, children: [] };
    }

    for (const id in family) {
        const parentId = family[id]?.parentId;
        if (parentId !== null) {
            family[parentId].children.push(family[id]);
        }
    }

    // Traverse the object hierarchy to print the output in the required format
    // this function implements a depth-first search algorithm. 
    // Specifically, it performs a pre-order traversal of the tree, 
    // where each node is visited before its children are visited.
    function printHierarchy(node, prefix = 0) {
        const dashes = '-'.repeat(prefix);
        console.log(dashes + node.name); // Visits the node BEFORE it's children
        node.children.forEach((child) => {
          printHierarchy(child, prefix + 1); // recursively visits it's children
        });
    }

    for (const id in family) {
        if (family[id]?.parentId === null) {
            printHierarchy(family[id]);
        }
    }

}

// getAnswerUsingFind(input);
getAnswerUsingForLoops(input);
