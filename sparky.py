import bpy


PI = 3.1415
ENCOGER_RUEDA = (1, 0.0805, 1)
ALTURA_RUEDA = 1

'''*********************************************************************'''
'''Funciones comunes útiles para selección/activación/borrado de objetos'''
'''*********************************************************************'''

def unirObjetos():
    bpy.ops.object.join()
    
def deseleccionarObjetos(): # Seleccionar un objeto por su nombre
    bpy.ops.object.select_all(action='DESELECT')

def seleccionarObjeto(nombreObjeto): # Seleccionar un objeto por su nombre
    bpy.data.objects[nombreObjeto].select_set(True)

def seleccionarUnicoObjeto(nombreObjeto): # Seleccionar un objeto por su nombre
    bpy.ops.object.select_all(action='DESELECT') # deseleccionamos todos...
    bpy.data.objects[nombreObjeto].select_set(True)

def activarObjeto(nombreObjeto): # Activar un objeto por su nombre
    bpy.context.scene.objects.active = bpy.data.objects[nombreObjeto]

def borrarObjeto(nombreObjeto): # Borrar un objeto por su nombre
    seleccionarObjeto(nombreObjeto)
    bpy.ops.object.delete(use_global=False)

def borrarObjetos(): # Borrar todos los objetos
    if(len(bpy.data.objects) != 0):
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete(use_global=False)

'''****************************************************************'''
'''Clase para realizar transformaciones sobre objetos seleccionados'''
'''****************************************************************'''
class Seleccionado:
    def mover(v):
        bpy.ops.transform.translate(
            value=v, constraint_axis=(True, True, True))

    def escalar(v):
        bpy.ops.transform.resize(value=v, constraint_axis=(True, True, True))

    def rotarX(v):
        bpy.ops.transform.rotate(value=v, orient_axis='X')

    def rotarY(v):
        bpy.ops.transform.rotate(value=v, orient_axis='Y')

    def rotarZ(v):
        bpy.ops.transform.rotate(value=v, orient_axis='Z')

'''**********************************************************'''
'''Clase para realizar transformaciones sobre objetos activos'''
'''**********************************************************'''
class Activo:
    def posicionar(v):
        bpy.context.object.location = v

    def escalar(v):
        bpy.context.object.scale = v

    def rotar(v):
        bpy.context.object.rotation_euler = v

    def renombrar(nombreObjeto):
        bpy.context.object.name = nombreObjeto
        
    def encoger(v):
        bpy.ops.transform.resize(value=v, orient_type='GLOBAL', 
        orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', 
        constraint_axis=(False, True, False), mirror=True, use_proportional_edit=False, 
        proportional_edit_falloff='SMOOTH', proportional_size=1, 
        use_proportional_connected=False, use_proportional_projected=False, 
        release_confirm=True)

'''**************************************************************'''
'''Clase para realizar transformaciones sobre objetos específicos'''
'''**************************************************************'''
class Especifico:
    def escalar(nombreObjeto, v):
        bpy.data.objects[nombreObjeto].scale = v

    def posicionar(nombreObjeto, v):
        bpy.data.objects[nombreObjeto].location = v

    def rotar(nombreObjeto, v):
        bpy.data.objects[nombreObjeto].rotation_euler = v
        
    def encoger(v):
        bpy.ops.transform.resize(value=v, orient_type='GLOBAL', 
        orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', 
        constraint_axis=(False, True, False), mirror=True, use_proportional_edit=False, 
        proportional_edit_falloff='SMOOTH', proportional_size=1, 
        use_proportional_connected=False, use_proportional_projected=False, 
        release_confirm=True)

'''************************'''
'''Clase para crear objetos'''
'''************************'''
class Objeto:
    def crearCubo(objName):
        bpy.ops.mesh.primitive_cube_add(size=0.5, location=(0, 0, 0))
        Activo.renombrar(objName)

    def crearEsfera(objName):
        bpy.ops.mesh.primitive_uv_sphere_add(radius=0.5, location=(0, 0, 0))
        Activo.renombrar(objName)

    def crearCono(objName):
        bpy.ops.mesh.primitive_cone_add(radius1=0.5, location=(0, 0, 0))
        Activo.renombrar(objName)
        
    def crearCilindro(objName):
        bpy.ops.mesh.primitive_cylinder_add(radius=1, depth=2, enter_editmode=False, location=(0, 0, 0))
        Activo.renombrar(objName)
        
    def crearIcoesfera(objName):
        bpy.ops.mesh.primitive_ico_sphere_add(radius=1, enter_editmode=False, location=(0, 0, 0))
        Activo.renombrar(objName)
        
    def crearTorus(objName):
        bpy.ops.mesh.primitive_torus_add(align='WORLD', location=(0, 0, 0), rotation=(0, 0, 0), major_radius=1, minor_radius=0.25, abso_major_rad=1.25, abso_minor_rad=0.75)
        Activo.renombrar(objName)


'''************'''
''' M  A  I  N '''
'''************'''
if __name__ == "__main__":
    # Creación de un cubo y transformaciones de este:
    
    borrarObjetos()

    """RUEDA IZQUIERDA"""
    
    Objeto.crearTorus("R11")
    Seleccionado.rotarX(PI/2)
    Activo.escalar((0.8,0.8,0.6))
    Activo.posicionar((0,1.8,ALTURA_RUEDA))
    
    Objeto.crearCilindro("R12")
    Seleccionado.rotarX(PI/2)
    Activo.encoger(ENCOGER_RUEDA)
    Activo.posicionar((0,1.65,ALTURA_RUEDA))
    
    Objeto.crearCilindro("R13")
    Seleccionado.rotarX(PI/2)
    Activo.encoger(ENCOGER_RUEDA)
    Activo.encoger((0.35,1,0.35))
    Activo.posicionar((0,1.8,ALTURA_RUEDA))
    
    
    Objeto.crearCilindro("R14")
    Seleccionado.rotarX(PI/2)
    Activo.encoger(ENCOGER_RUEDA)
    Activo.encoger((0.1,5,0.1))
    Activo.posicionar((0,1.5,ALTURA_RUEDA))

    
    seleccionarObjeto("R11")
    seleccionarObjeto("R13")
    unirObjetos()
    
    seleccionarObjeto("R12")
    seleccionarObjeto("R14")
    unirObjetos()
    
    """RUEDA DERECHA"""

    Objeto.crearTorus("R21")
    Seleccionado.rotarX(PI/2)
    Activo.escalar((0.8,0.8,0.6))
    Activo.posicionar((0,-1.8,ALTURA_RUEDA))
    
    Objeto.crearCilindro("R22")
    Seleccionado.rotarX(PI/2)
    Activo.encoger(ENCOGER_RUEDA)
    Activo.posicionar((0,-1.65,ALTURA_RUEDA))
    
    Objeto.crearCilindro("R23")
    Seleccionado.rotarX(PI/2)
    Activo.encoger(ENCOGER_RUEDA)
    Activo.encoger((0.35,1,0.35))
    Activo.posicionar((0,-1.8,ALTURA_RUEDA))
    
    Objeto.crearCilindro("R24")
    Seleccionado.rotarX(PI/2)
    Activo.encoger(ENCOGER_RUEDA)
    Activo.encoger((0.1,5,0.1))
    Activo.posicionar((0,-1.5,ALTURA_RUEDA))

    
    seleccionarObjeto("R21")
    seleccionarObjeto("R23")
    unirObjetos()
    
    seleccionarObjeto("R22")
    seleccionarObjeto("R24")
    unirObjetos()
    
    """CUERPO"""


    Objeto.crearCubo("C1")
    Activo.escalar((3.8,3.8,3.8))
    Activo.encoger((1.25,1,0.3))
    Activo.posicionar((0,0,1.15))
    
    Objeto.crearCubo("C2")
    Activo.escalar((3.8,3.8,3.8))
    Activo.encoger((1,1.25,0.3))
    Activo.posicionar((0,0,1.15))
    
    Objeto.crearCubo("C3")
    Activo.escalar((3.8,3.8,3.8))
    Activo.encoger((0.95,0.7,0.4))
    Activo.posicionar((0,0,1.75))
    
    seleccionarObjeto("C1")
    seleccionarObjeto("C2")
    seleccionarObjeto("C3")
    unirObjetos()
    
    """CANON"""
    
    Objeto.crearIcoesfera("L1")
    Activo.posicionar((0.2,0,3.1))
    
    Objeto.crearIcoesfera("L2")
    Activo.posicionar((1,0,3.1))
    Activo.escalar((1.35,1,1))
    
    Objeto.crearIcoesfera("L3")
    Activo.posicionar((1.5,0,3.1))
    Activo.escalar((1.75,0.7,0.8))
    
    seleccionarObjeto("L1")
    seleccionarObjeto("L2")
    seleccionarObjeto("L3")
    unirObjetos()

    """AROS"""
    
    Objeto.crearCubo("B1")
    Activo.posicionar((0.1,0,3.9))
    
    Objeto.crearTorus("T1")
    Activo.posicionar((2.25,0,3.15))
    Activo.escalar((0.8,0.8,0.8))
    Seleccionado.rotarY(PI/2)
    
    Objeto.crearTorus("T2")
    Activo.posicionar((2.5,0,3.15))
    Activo.escalar((0.7,0.7,0.7))
    Seleccionado.rotarY(PI/2)
    
    Objeto.crearTorus("T3")
    Activo.posicionar((2.75,0,3.15))
    Activo.escalar((0.6,0.6,0.6))
    Seleccionado.rotarY(PI/2)
    
    Objeto.crearTorus("T4")
    Activo.posicionar((2.95,0,3.15))
    Activo.escalar((0.45,0.45,0.45))
    Seleccionado.rotarY(PI/2)
    
    Objeto.crearTorus("T5")
    Activo.posicionar((3.1,0,3.15))
    Activo.escalar((0.4,0.4,0.4))
    Seleccionado.rotarY(PI/2)
    
    seleccionarObjeto("T1")
    seleccionarObjeto("T2")
    seleccionarObjeto("T3")
    seleccionarObjeto("T4")
    seleccionarObjeto("T5")
    unirObjetos()

    """BANDERA"""
    
    Objeto.crearCilindro("PB1")
    Activo.posicionar((-0.85,1,3.95))
    Activo.escalar((0.05,0.05,2.5))
    
    Objeto.crearCubo("B1")
    Activo.posicionar((-2.2,1,4.25))
    Activo.escalar((6,0.05,2))
    
    Objeto.crearCubo("B2")
    Activo.posicionar((-2.2,1,5.25))
    Activo.escalar((6,0.05,2))
    
    """CAMARA"""
    
    Objeto.crearCubo("H1")
    Seleccionado.rotarY(-PI/4)
    Activo.posicionar((0.2,0,4.3))
    Activo.escalar((0.4,0.8,1))
    
    Objeto.crearCilindro("H2")
    Activo.posicionar((0.4,0,4.5))
    Activo.escalar((0.12,0.3,0.2))
    Seleccionado.rotarY(-PI/2)
    
    Objeto.crearTorus("H3")
    Activo.posicionar((0.6,0.05,4.5))
    Activo.escalar((0.06,0.06,0.1))
    Seleccionado.rotarY(-PI/2)
    
    Objeto.crearTorus("H4")
    Activo.posicionar((0.6,-0.15,4.5))
    Activo.escalar((0.03,0.03,0.1))
    Seleccionado.rotarY(-PI/2)
    
    Objeto.crearTorus("H5")
    Activo.posicionar((0.6,0.05,4.5))
    Activo.escalar((0.02,0.02,0.1))
    Seleccionado.rotarY(-PI/2)
    
    
    
    
    