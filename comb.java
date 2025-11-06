import java.util.*;

public class Combinations {
    public static List<List<Integer>> getCombinations(int n, int k) {
        List<List<Integer>> res = new ArrayList<>();
        backtrack(res, new ArrayList<>(), n, 1, k);
        return res;
    }

    private static void backtrack(List<List<Integer>> res, List<Integer> combo, int n, int start, int k) {
        if (combo.size() == k) {
            res.add(new ArrayList<>(combo));
            return;
        }
        for (int i = start; i <= n; ++i) {
            combo.add(i);
            backtrack(res, combo, n, i + 1, k);
            combo.remove(combo.size() - 1);
        }
    }

    public static void main(String[] args) {
        System.out.println(getCombinations(3, 2));
    }
}
