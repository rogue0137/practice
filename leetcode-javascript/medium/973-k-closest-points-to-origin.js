/**
 * @param {number[][]} points
 * @param {number} k
 * @return {number[][]}
 */

const computedDistance = (points) => {
    const x = points[0] * points[0];
    const y = points[1] * points[1];

    return x + y;
}

const kClosest = function(points, numPointsToReturn) {

    const pointsLen = points.length;
    if (numPointsToReturn === pointsLen) return points;

    let listOfPointsWithTheirDistances = [];

    for (let i = 0; i < pointsLen; i++){
        listOfPointsWithTheirDistances.push({
            points: points[i],
            distance: computedDistance(points[i])
        })
    }

    listOfPointsWithTheirDistances.sort((a, b) => a.distance - b.distance);

    let closestPoints = [];

    for (let j = 0; j < numPointsToReturn; j++) {
        closestPoints.push(listOfPointsWithTheirDistances[j].points);
    }

    return closestPoints;
};
