class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        # Augment the string as per the problem description
        t = "1" + s + "1"
        
        # Group contiguous characters
        groups = []
        count = 1
        for i in range(1, len(t)):
            if t[i] == t[i-1]:
                count += 1
            else:
                groups.append((t[i-1], count))
                count = 1
        groups.append((t[-1], count))
        
        # Extract the lengths of '0' blocks and '1' blocks
        Z = []
        O = []
        for val, c in groups:
            if val == '0':
                Z.append(c)
            else:
                O.append(c)
                
        # The internal '1' blocks exclude the augmented ends
        internal_O = O[1:-1]
        
        initial_ones = s.count('1')
        
        # If there are no internal blocks of '1's, no trade can be made
        if not internal_O:
            return initial_ones
            
        # To optimize Option 2, find the top 3 largest '0' blocks
        # 3 is sufficient to guarantee we find a valid block not equal to i or i+1
        top3_Z = sorted([(z, idx) for idx, z in enumerate(Z)], reverse=True)[:3]
        
        max_gain = 0
        
        # Evaluate trades over every internal '1' block
        for i in range(len(internal_O)):
            # Option 1: Target the newly merged 0-block
            gain1 = Z[i] + Z[i+1]
            
            # Option 2: Target the largest completely distinct 0-block elsewhere
            gain2 = 0
            for z_val, z_idx in top3_Z:
                if z_idx != i and z_idx != i + 1:
                    gain2 = z_val - internal_O[i]
                    break  # Since top3_Z is sorted descending, the first valid is the largest
                    
            max_gain = max(max_gain, gain1, gain2)
            
        return initial_ones + max_gain