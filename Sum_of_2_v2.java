public class Solution {
	public ArrayList<Integer> twoSum(final List<Integer> a, int b) {
	    
	    ArrayList<Integer> ans = new ArrayList<>();
	    
	    int sum = 0;
	    
	    HashMap<Integer,ArrayList<Integer>> m = new HashMap<>();
	    
	    for(int i=0;i < a.size() ; i++){
	        
	  
	        ArrayList<Integer> temp = new ArrayList<>();
	        if(m.containsKey(a.get(i)  )){
	            temp = m.get(a.get(i));
	        }
	        
	        temp.add(i+1);
	        m.put(a.get(i),temp);
	    }
	    
	    int i2 = a.size();
	    int i1 = 0;
	    int c1,c2;
	    
	    for(int j=0; j < a.size();j++){
	        
	        //System.out.println(m.get(2) );
	        if(m.containsKey(b - a.get(j)) && b-a.get(j) != a.get(j)   ){
	             c2 = m.get(b-a.get(j)).get(0);
	            
	            
	             c1 = j+1;
	            
	            if(c1 > c2){
	                c1 = c1+c2;
	                c2 = c1 - c2;
	                c1 = c1 - c2;
	            }
	            
	            if(c2 < i2){ i2 = c2 ; i1 = c1;}
	            //if(c1 < i1){ i2 = c2 ; i1 = c1;}
	   }else if (m.containsKey(b - a.get(j)) && b-a.get(j) == a.get(j) &&  m.get(b-a.get(j)).size() > 1 ){
	            c1 = m.get(b-a.get(j)).get(0);
	            c2 = m.get(b-a.get(j)).get(1);
	            
	            if(c1 > c2){
	                c1 = c1+c2;
	                c2 = c1 - c2;
	                c1 = c1 - c2;
	            }
	            
	            if(c2 < i2){ i2 = c2 ; i1 = c1;}
	            
	        }
	        
	    }
	    
	    if(i1 == 0 && i2 == a.size()) return ans;
	    
	    if(i1 > i2){
	        ans.add(i2);
	        ans.add(i1);
	    }else{
	        ans.add(i1);
	        ans.add(i2);
	    }
	    
	    return ans;
	}
}
