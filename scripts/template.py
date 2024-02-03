

def copy_slide_from_external_prs(self, slideNumber:int):

    # source is example.pptx
    src = Presentation("example.pptx")
    
    # specify the slide you want to copy the contents from
    src_slide = src.slides[slideNumber - 1]

    # # Define the layout you want to use from your generated pptx
    # SLD_LAYOUT = 5
    # slide_layout = prs.slide_layouts[SLD_LAYOUT]

    # create now slide, to copy contents to
    curr_slide = self.presentation.slides.add_slide()

    # create images dict
    imgDict = {}

    # now copy contents from external slide, but do not copy slide properties
    # e.g. slide layouts, etc., because these would produce errors, as diplicate
    # entries might be generated
    for shp in src_slide.shapes:
        if 'Picture' in shp.name:
            # save image
            with open(shp.name+'.jpg', 'wb') as f:
                f.write(shp.image.blob)

            # add image to dict
            imgDict[shp.name+'.jpg'] = [shp.left, shp.top, shp.width, shp.height]
        else:
            # create copy of elem
            el = shp.element
            newel = copy.deepcopy(el)

            # add elem to shape tree
            curr_slide.shapes._spTree.insert_element_before(newel, 'p:extLst')

    # add pictures
    for k, v in imgDict.items():
        curr_slide.shapes.add_picture(k, v[0], v[1], v[2], v[3])
        os.remove(k)