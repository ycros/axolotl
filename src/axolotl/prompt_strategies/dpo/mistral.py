def prompt_pairs(cfg):  # pylint: disable=possibly-unused-variable,unused-argument
    def transform_fn(sample):
        if "system" in sample and sample["system"]:
            sample["prompt"] = (
                f"[INST] {sample['system']} [/INST]</s> "
                f"[INST] {sample['prompt']} [/INST]"
            )
        else:
            sample["prompt"] = f"[INST] {sample['prompt']} [/INST]"
        sample["chosen"] = f" {sample['chosen']}</s>"
        sample["rejected"] = f" {sample['rejected']}</s>"
        return sample

    return transform_fn
