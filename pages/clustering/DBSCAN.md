---
id: DBSCAN
aliases: []
tags: []
index: 7
---

# DBSCAN (DENSITY BASED SPATIAL CLUSTERING OF APPLICATION WITH NOISE)

## DEFINITIONS

Define $\epsilon$ as the radius of an hypersphere  and a $minPoints$ threshold value

- ### CORE

	a point with $n > minPoints$ points inside is hypersphere of $\epsilon$ radius

- ###  BORDER

	a point with $n < minPoints$ points inside is hypersphere of $\epsilon$ radius

- ###  NEIGHBORHOOD

	two points are in neighborhood with each other when they are inside each hypersphere

- ### DIRECT DENSITY REACHABILITY

	a point $p$ is in direct density reachable with a point $q$ when $q$ is core and $p$ is in $q$ neighborhood

- ###  DENSITY REACHABILITY

	a point $p$ is in density reachable with a point $q$ when  and $p$  are connected by a series of direct density reachable points $q_{n}$

- ### DENSITY CONNECTION

	a point $p$ is density connected to point $q$ if there is a point $s$ such that $p$ and $q$ are density reachable from $s$


## ALGORITHM

```python
Algorithm 1 DBSCAN
Require: SetOfPoints: UNCLASSIfIED points
Require: Eps, MinPts
	ClusterId <- nextId(NOISE);
	for i = 1 to SetOfPoints.size do
		Point <- SetOfPoints.get(i)
		if Point.ClId = UNCLASSIfIED then
			if ExpandCluster(SetOfPoints, Point, ClusterId, Eps, MinPts) then
				ClusterId <- nextId(ClusterId)
Ensure: SetOfPoints
```

```python
ExpandCluster(SetOfPoints, Point, ClId, Eps, MinPts) : Boolean;
	seeds:=SetOfPoints.regionQuery(Point,Eps);
	If seeds.size<MinPts THEN # no core point
		SetOfPoint.changeClId(Point,NOISE);
		RETURN False;
	ELSE
# all points in seeds are density-reachable from Point
		SetOfPoints.changeClIds(seeds,ClId);
		seeds.delete(Point);
		WHILE seeds <> Empty DO
			currentP := seeds.first();
			result := SetOfPoints.regionQuery(currentP,Eps);
			If result.size >= MinPts THEN
				For i FROM 1 TO result.size DO
					resultP := result.get(i);
					If resultP.ClId IN {UNCLASSIfIED, NOISE} THEN
						If resultP.ClId = UNCLASSIfIED THEN seeds.append(resultP);
						END If;
						SetOfPoints.changeClId(resultP,ClId);
					END If; # UNCLASSIfIED or NOISE
				END For;
			END If; # result.size >= MinPts
			seeds.delete(currentP);
		END WHILE; # seeds <> Empty
		RETURN True;
	END If
END; # ExpandCluster
```

## PARAMETERS TO TUNE

$\epsilon$ and $minPoints$ are the parameter that need to be tuned, a good value for $minPoints$ can be $2*D$ where $D$ is the number of dimensions

[PREVIOUS](DENSITY_BASED_CLUSTERING.md)
