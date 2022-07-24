import sys
class Solution:
    def commonElements (self,A, B, C, n1, n2, n3):
        # your code here
        i,j,k=0,0,0
        prev1,prev2,prev3=-sys.maxsize-1,-sys.maxsize-1,-sys.maxsize-1
        common_elems=[]
        while i<n1 and j<n2 and k<n3:
            
            while i<n1 and A[i]==prev1:
                i+=1
            
            while j<n2 and B[j]==prev2:
                j+=1
            
            while k<n3 and C[k]==prev3:
                k+=1
            
            if i==n1 or j==n2 or k==n3:
                break
        
            if A[i]==B[j] and B[j]==C[k]:
                common_elems.append(A[i])
                prev1=A[i]
                prev2=B[j]
                prev3=C[k]
                i+=1
                j+=1
                k+=1
            
            elif A[i]<B[j]:
                prev1=A[i]
                i+=1
            elif B[j]<C[k]:
                prev2=B[j]
                j+=1
            else:
                prev3=C[k]
                k+=1
        
        return common_elems

ob = Solution()
A=[3,3,3]
B=[3,3,3]
C=[3,3,3]
print(ob.commonElements(A,B,C,3,3,3))
