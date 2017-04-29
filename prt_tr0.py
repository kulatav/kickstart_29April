from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def prt_tr0():
    if request.method == 'POST':
        if request.form['submit'] == 'Save':
            fi = open('prt_ks.cfg', 'w')
            if request.form.get("prt_check_zerombr"):
                fi.write("\n#Clear master boot record \nzerombr")
            if request.form.get("prt_check_rmallpart"):
                fi.write("\n#Partition Clearing Information\nclearpart --all")
                if request.form.get("prt_check_initlabel"):
                    fi.write(" --initlabel")
            else:
                fi.write("\n#Partition Clearing Information\nclearpart --none")
            if request.form.get("prt_check_autopart"):
                fi.write("\n#Disk partitioning information \nautopart")
            else:
                all_vg = request.form['prt_all_vg']
                all_lv = request.form['prt_all_lv']
                vg_list = all_vg.split("$$")
                lv_list = all_lv.split("$$")
                t1=len(vg_list)
                t2=len(lv_list)
                i=0
                fi.write("\n#Disk partitioning information")
                for i in range(t1):
                    if i!=0:
                        vg_field=vg_list[i].split(" ")
                        vg_name=vg_field[1].split(":")
                        vg_disk=vg_field[2].split(":")
                        vg_size=vg_field[3].split(":")
                        vg_pesize=vg_field[4].split(":")
                        fi.write("\npart pv_"+vg_name[1]+' --fstype="lvmpv" --ondisk='+vg_disk[1]+" --size="+vg_size[1])
                        fi.write("\nvolgroup "+vg_name[1]+" --pesize="+vg_pesize[1]+" pv_"+vg_name[1])
                for i in range(t2):
                    if i!=0:
                        lv_field = lv_list[i].split(" ")
                        lv_mnt_pt = lv_field[1].split(":")
                        lv_vg = lv_field[2].split(":")
                        lv_name = lv_field[3].split(":")
                        lv_fst = lv_field[4].split(":")
                        lv_size = lv_field[5].split(":")
                        fi.write("\nlogvol " + lv_mnt_pt[1] + " --vgname=" + lv_vg[1] + " --name=" + lv_name[
                            1] + " --fstype=" + lv_fst[1] + " --size=" + lv_size[1])
                        if (len(lv_field) == 8):
                            lv_maxsize = lv_field[7].split(":")
                            fi.write(" --grow --maxsize=" + lv_maxsize[1])
            fi.close()
            return render_template('part_tr0.html')
    elif request.method == 'GET':
        return render_template('part_tr0.html')

if __name__ == '__main__':
    app.run(debug='true');