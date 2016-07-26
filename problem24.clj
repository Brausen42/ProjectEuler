(defn remove_element
  [n lis]
  (into [] (concat (subvec lis 0 n) (subvec lis (inc n)))))

(defn map_to_front
  [h lis]
  (into [] (map #(into [] (concat [h] %)) lis)))

(defn permute
  [lis]
  (if (<= (count lis) 1)
    [lis]
    (loop [[h & tail] (range (count lis))
           perms []]
      (if (empty? tail)
        (concat perms (map_to_front (get lis h) (permute (remove_element h lis))))
        (recur tail (concat perms (map_to_front (get lis h) (permute (remove_element h lis)))))))))

(remove_element 0 [1 2 3 4 5])

(map_to_front 0 [[1 2 3] [4 5 6]])

(count (permute [0 1 2 3 4 5 6 7 8 9]))
