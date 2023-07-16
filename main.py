import vtk

def main():
    reader = vtk.vtkNrrdReader()
    reader.SetFileName("Data/transformed_image.nrrd")

    window = vtk.vtkRenderWindow()
    renderer = vtk.vtkRenderer()

    window.AddRenderer(renderer)

    interactor = vtk.vtkRenderWindowInteractor()
    window.SetInteractor(interactor)

    contour = vtk.vtkContourFilter()
    contour.SetInputConnection(reader.GetOutputPort())
    contour.SetValue(0, 135)

    contourMapper = vtk.vtkPolyDataMapper()
    contourMapper.SetInputConnection(contour.GetOutputPort())
    contourMapper.ScalarVisibilityOff()
    
    contourActor = vtk.vtkActor()
    contourActor.SetMapper(contourMapper)

    renderer.AddActor(contourActor)

    window.Render()
    interactor.Start()


if __name__ == "__main__":
    main()
