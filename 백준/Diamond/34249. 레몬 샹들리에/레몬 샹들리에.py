MOD=10**9+7
N=int(input().strip())
if N==0:
    print(0)
else:
    inv=[0]*(N+1)
    inv[1]=1
    for i in range(2,N+1):
        inv[i]=(MOD-MOD//i)*inv[MOD%i]%MOD
    invN=pow(N,MOD-2,MOD)
    C_prev=1
    P_prev=1
    ans=0
    for k in range(1,N+1):
        Ck=C_prev*(N-k+1)%MOD*inv[k]%MOD
        Pk=P_prev*(N-k+1)%MOD
        term=invN*Ck%MOD*C_prev%MOD
        ans=(ans+term*Pk)%MOD
        C_prev=Ck
        P_prev=Pk
    print(ans%MOD)
