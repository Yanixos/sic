#!/usr/bin/python3.6

try :
    import hashlib, os, sys, db, crypt
except ImportError as e :
    print("[!] Missing module : ",e)
    sys.exit(1)


def FileAttributes(hash,name,table_name) :

    file_path = str(name) 
    file_hash = str(hash)   
    file_inode = str(os.stat(name).st_ino)  
    file_permission = str(os.stat(name).st_mode)
    file_uid = str(os.stat(name).st_uid)  
    file_gid = str(os.stat(name).st_gid) 
    file_reference = str(os.stat(name).st_nlink) 
    file_table = str(table_name)
    check_some = file_inode+file_permission+file_uid+file_gid 
    check_some = hashlib.sha256(check_some.encode()).hexdigest() 
    row=()      
    row =(file_path,file_hash,check_some,file_inode,file_permission,file_uid,file_gid,file_reference,file_table)
    
    return row

def HashFile(f,hasher):

        with open(f,'rb') as fr :
                  hasher = hashlib.new(hasher,fr.read()).hexdigest()
        return hasher

def HashDir(dir,table_name,hasher,verbose,update_check):

    total_paths = 0
    if update_check == 1 :   
          fwa = open('/usr/share/sic/ActualBase.list','a')
          os.chmod('/usr/share/sic/ActualBase.list',0o600)
    else : 
          update = True
          fw = open('/usr/share/sic/.DirArchi/.'+table_name,'w')  
          os.chmod('/usr/share/sic/.DirArchi/.'+table_name,0o600)
    for rootDir , subDirs , subFiles in os.walk(dir) :
    
            for i in range(0,len(subFiles)) :
                f = str(rootDir)+'/'+str(subFiles[i])
                total_paths += 1

                if '.log' in f or 'log/' in f or 'spool/' in f or 'history' in f or 'cache' in f or '/var/lib' in f or 'mtab' in f or 'backup' in f or 'subscriptions.conf' in f or '/etc/resolv.conf' in f or 'mail' in f :
                     pass
                else :
                      try :
                            hash = HashFile(f,hasher)
                      except Exception as e :
                            pass
                      row = FileAttributes(hash,f,table_name)
                      if update_check == 0 :
                            db.insert_table(table_name,row,verbose)
                            fw.write(f+"\n")
                      else :
                            fwa.write(str(row)[1:-1]+"\n")
    if update_check == 1 :
          fwa.close()
    else :
          fw.close()
             
    return total_paths
