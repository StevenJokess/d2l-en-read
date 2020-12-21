

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-22 01:26:33
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-22 01:26:33
 * @Description:
 * @TODO::
 * @Reference:https://github.com/zhreshold/mxnet-ssd/blob/master/deploy.py
-->
    args = parse_args()
    net = get_symbol(args.network, args.data_shape,
        num_classes=args.num_classes, nms_thresh=args.nms_thresh,
        force_suppress=args.force_nms, nms_topk=args.nms_topk)
    if args.prefix.endswith('_'):
        prefix = args.prefix + args.network + '_' + str(args.data_shape)
    else:
        prefix = args.prefix
    _, arg_params, aux_params = mx.model.load_checkpoint(prefix, args.epoch)
    # new name
    tmp = prefix.rsplit('/', 1)
    save_prefix = '/deploy_'.join(tmp)
    mx.model.save_checkpoint(save_prefix, args.epoch, net, arg_params, aux_params)
    print("Saved model: {}-{:04d}.params".format(save_prefix, args.epoch))
    print("Saved symbol: {}-symbol.json".format(save_prefix))
