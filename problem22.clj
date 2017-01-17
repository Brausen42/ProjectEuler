(require '[clojure.string :as str])

(defn get_strings_from_cvs_file
  [filename]
  (str/split
    (slurp filename)
    #","))

(defn string_to_int
  [string]
  (reduce +
    (map (fn [n] (- (int n) 64)) string)))

(loop [remaining (map
                   #(string_to_int %)
                   (sort
                     (map
                       #(clojure.string/replace % #"\"" "")
                       (get_strings_from_cvs_file "C:\\Users\\uc215061\\Documents\\Clojure\\names.txt"))))
       total 0
       index 1]
  (if (empty? remaining)
    total
    (let [[h & remain] remaining]
      (recur remain (+ total (* h index)) (inc index)))))
