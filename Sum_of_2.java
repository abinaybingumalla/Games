public class Solution {
    
    static class Node implements Comparable<Node> {
        
        int left;
        int right;
        
        public Node(int left, int right) {
            this.left = left;
            this.right  = right;
        }
        
        public int compareTo(Node o) {
            if (this.right < o.right)
                return -1;
            if (this.right > o.right)
                return 1;
                
            return Integer.compare(this.left, o.left);
        }
        
    }
    
	public ArrayList<Integer> twoSum(final List<Integer> A, int B) {
	    
	    int sum = B;
	    int diff;
	    HashMap<Integer, Integer> hashMap = new HashMap<Integer, Integer>();
	    int size = A.size();
	    int num;
	    int index;
	    ArrayList<Integer> res = new ArrayList<Integer>();
        ArrayList<Node> node = new ArrayList<>();
	    
	    for (int i = size - 1; i >= 0; i--) {
	        num = A.get(i);
	        diff = sum - num;
	        
	        if (hashMap.containsKey(diff)) {
	            index = hashMap.get(diff);
	            node.add(new Node(i + 1, index + 1));
	        }
	        
	        hashMap.put(num, i);
	        
	    }
	    
	    if (node.size() > 0) {
	        Collections.sort(node);
            res.add(node.get(0).left);
            res.add(node.get(0).right);
	    }
	    
	    return res;
	    
	}
}