from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *

mdb.models[’Model-1’].ConstrainedSketch(name=’__profile__’, sheetSize=20.0)
mdb.models[’Model-1’].sketches[’__profile__’].rectangle(point1=(-5.0, -1.0),
point2=(5.0, 1.0))
mdb.models[’Model-1’].Part(dimensionality=TWO_D_PLANAR, name=’Part-1’, type=
DEFORMABLE_BODY)
mdb.models[’Model-1’].parts[’Part-1’].BaseShell(sketch=
mdb.models[’Model-1’].sketches[’__profile__’])
del mdb.models[’Model-1’].sketches[’__profile__’]

mdb.models[’Model-1’].Material(name=’Material-1’)
mdb.models[’Model-1’].materials[’Material-1’].Elastic(table=((1000000000.0,
0.3), ))
mdb.models[’Model-1’].HomogeneousSolidSection(material=’Material-1’, name=
’Section-1’, thickness=None)
mdb.models[’Model-1’].parts[’Part-1’].SectionAssignment(offset=0.0,
offsetField=’’, offsetType=MIDDLE_SURFACE, region=Region(
faces=mdb.models[’Model-1’].parts[’Part-1’].faces.findAt(((-1.666667,
-0.333333, 0.0), (0.0, 0.0, 1.0)), )), sectionName=’Section-1’)

mdb.models[’Model-1’].parts[’Part-1’].Set(edges=
mdb.models[’Model-1’].parts[’Part-1’].edges.findAt(((-5.0, -0.5, 0.0), )),
name=’Set-1’)
mdb.models[’Model-1’].parts[’Part-1’].Surface(name=’Surf-1’, side1Edges=
mdb.models[’Model-1’].parts[’Part-1’].edges.findAt(((-2.5, 1.0, 0.0), )))

mdb.models[’Model-1’].parts[’Part-1’].setMeshControls(elemShape=QUAD, regions=
mdb.models[’Model-1’].parts[’Part-1’].faces.findAt(((-1.666667, -0.333333,
0.0), )), technique=STRUCTURED)
mdb.models[’Model-1’].parts[’Part-1’].setElementType(elemTypes=(ElemType(
elemCode=CPS8R, elemLibrary=STANDARD), ElemType(elemCode=CPS6M,
elemLibrary=STANDARD)), regions=(
mdb.models[’Model-1’].parts[’Part-1’].faces.findAt(((-1.666667, -0.333333,
0.0), )), ))
mdb.models[’Model-1’].parts[’Part-1’].seedPart(deviationFactor=0.1, size=0.5)
mdb.models[’Model-1’].parts[’Part-1’].generateMesh()

mdb.models[’Model-1’].rootAssembly.DatumCsysByDefault(CARTESIAN)
mdb.models[’Model-1’].rootAssembly.Instance(dependent=ON, name=’Part-1-1’,
part=mdb.models[’Model-1’].parts[’Part-1’])
mdb.models[’Model-1’].rootAssembly.regenerate()

mdb.models[’Model-1’].StaticStep(initialInc=0.1, maxInc=0.1, name=’Step-1’,
previous=’Initial’)
mdb.models[’Model-1’].DisplacementBC(amplitude=UNSET, createStepName=’Step-1’,
distributionType=UNIFORM, fieldName=’’, fixed=OFF, localCsys=None, name=
’BC-1’, region=
mdb.models[’Model-1’].rootAssembly.instances[’Part-1-1’].sets[’Set-1’], u1=
0.0, u2=0.0, ur3=0.0)
mdb.models[’Model-1’].Pressure(amplitude=UNSET, createStepName=’Step-1’,
distributionType=UNIFORM, field=’’, magnitude=-100000.0, name=’Load-1’,
region=
mdb.models[’Model-1’].rootAssembly.instances[’Part-1-1’].surfaces[’Surf-1’])

mdb.Job(contactPrint=OFF, description=’’, echoPrint=OFF, explicitPrecision=
SINGLE, historyPrint=OFF, memory=90, memoryUnits=PERCENTAGE, model=
’Model-1’, modelPrint=OFF, multiprocessingMode=DEFAULT, name=’EXAMPLE’,
nodalOutputPrecision=SINGLE, numCpus=1, numDomains=1,
parallelizationMethodExplicit=DOMAIN, scratch=’’, type=ANALYSIS,
userSubroutine=’’)
mdb.jobs[’EXAMPLE’].submit(consistencyChecking=OFF)


