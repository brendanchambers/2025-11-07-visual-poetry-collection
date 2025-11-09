



from omegaconf import DictConfig, OmegaConf
import hydra


def trim_first_and_last_page_from_pdf_singlepages(config, dir_path):

    import os
    singlepages_path = os.path.join(dir_path, "pdfs_singlepage")
    fnames = sorted(os.listdir(singlepages_path), reverse=True)

    tag = config.visual_poetry.p0_affix
    for fn in fnames:

        if tag in fn:  # if this is p0
            pdf_prefix = fn.split(tag)[0]
            pdf_pages = sorted([fn for fn in fnames if pdf_prefix in fn])

            try:
                last_page = pdf_pages.pop(-1)  # footer info on last page
                footer = os.path.join(dir_path, "pdfs_singlepage", last_page)
                os.remove(footer)
            except:
                print(f"failed to remove last page for {fn}")

            try:
                first_page = pdf_pages.pop(0)   # header info on first page
                header = os.path.join(dir_path, "pdfs_singlepage", first_page)
                os.remove(header)
            except:
                print(f"failed to remove first page for {fn}")

            

        fnames.remove(fn)  # already checked
                
def pdf2png(config, dir_path):

    import os
    from pdf2image import convert_from_path
    singlepages_path = os.path.join(dir_path, "pdfs_singlepage")
    fnames = sorted(os.listdir(singlepages_path), reverse=True)
    
    png_path = os.path.join(dir_path, "pngs_singlepage")
    os.makedirs(png_path, exist_ok=True)
    for fn in fnames:          
        fn_png = convert_from_path(os.path.join(singlepages_path, fn))[0]
        fn_png.save(os.path.join(png_path, fn.replace(".pdf", ".png")))


@hydra.main(version_base=None, config_path="<parentdir>", config_name="<configname>.yaml")
def preprocess_visual_poetry(cfg: DictConfig):

    # todo get this from config
    dataset_dir_path = "/Users/bc/brendanchambers/2025-11-07-visual-poetry-collection/data/intermediates/visual_poetry"
    trim_first_and_last_page_from_pdf_singlepages(cfg, dataset_dir_path)
    pdf2png(cfg, dataset_dir_path)

if __name__ == "__main__":
    preprocess_visual_poetry()