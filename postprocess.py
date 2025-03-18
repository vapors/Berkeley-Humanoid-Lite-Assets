import datetime

urdf_path = "data/urdf/robot.urdf"

# update URDF mesh directory
with open(urdf_path, "r") as f:
    content = f.read()

now = datetime.datetime.now().strftime("%Y-%m-%d")

content = content.replace("package://", "../meshes")
content = content.replace("<robot name=\"berkeley-humanoid-lite\">", """<robot name=\"berkeley-humanoid-lite\" version=\"{0}\">
  <mujoco>
    <compiler meshdir="../meshes/" balanceinertia="true" discardvisual="false"/>
  </mujoco>""".format(now))

with open(urdf_path, "w") as f:
    f.write(content)
