#Exercise:Count Inversion
"""
Given an array A of size N ,count the number of inversion .
Q. What is Inversion?
ans. i<j but A[i]>=A[j]
"""
long long merge(vector<int>&arr, vector<int>&temp, int start, int mid, int end){
    int i = start;
    int j = mid;
    int k = start;
    long long invcount = 0;
    while(i<=mid-1 && j<=end){
        if(arr[j] >= arr[i]){
            temp[k] = arr[i];
            k++;
            i++;
        }
        else{
            invcount += mid-i;
            temp[k] = arr[j];
            k++;
            j++;
        }
    }
    while(i <= mid-1){
        temp[k]=arr[i];
        k++;
        i++;
    }
    while(j <= end){
        temp[k] = arr[j];
        k++;
        j++;
    }
    for(int i=start; i<=end; i++){
        arr[i] = temp[i];
    }
    return invcount%1000000007;
    
}
long long mergeSort(vector<int>&arr, vector<int>&temp, int start, int end){
    long long invcount = 0;
    long long mod =1000000007;
    if(start < end){
        
        int mid = start + (end-start)/2;
        invcount += mergeSort(arr, temp, start, mid)%mod;
        invcount += mergeSort(arr, temp, mid+1, end)%mod;
        
        invcount += merge(arr, temp, start, mid+1, end)%mod;
    }
    
    return invcount%mod;
    
}
int Solution::solve(vector<int>& arr){
   vector<int> temp;
    int n = arr.size();
    for(int i=0; i<n; i++){
        temp.push_back(0);
    }
    long long ans = mergeSort(arr, temp, 0, n-1);
    return ans;
}

