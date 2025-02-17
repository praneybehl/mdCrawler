Skip to content 
Version Notice
This documentation is ahead of the last release by 8 commits. You may see documentation for features not yet supported in the latest release v0.0.24 2025-02-12. 
# `pydantic_ai.agent`
###  Agent `dataclass`
Bases: `Generic[AgentDepsT, ResultDataT]`
Class for defining "agents" - a way to have a specific type of "conversation" with an LLM.
Agents are generic in the dependency type they take `AgentDepsT` and the result data type they return, `ResultDataT`.
By default, if neither generic parameter is customised, agents have type `Agent[None, str]`.
Minimal usage example:
```
from pydantic_ai import Agent
agent = Agent('openai:gpt-4o')
result = agent.run_sync('What is the capital of France?')
print(result.data)
#> Paris

```

Source code in `pydantic_ai_slim/pydantic_ai/agent.py`
```
 63
 64
 65
 66
 67
 68
 69
 70
 71
 72
 73
 74
 75
 76
 77
 78
 79
 80
 81
 82
 83
 84
 85
 86
 87
 88
 89
 90
 91
 92
 93
 94
 95
 96
 97
 98
 99
 100
 101
 102
 103
 104
 105
 106
 107
 108
 109
 110
 111
 112
 113
 114
 115
 116
 117
 118
 119
 120
 121
 122
 123
 124
 125
 126
 127
 128
 129
 130
 131
 132
 133
 134
 135
 136
 137
 138
 139
 140
 141
 142
 143
 144
 145
 146
 147
 148
 149
 150
 151
 152
 153
 154
 155
 156
 157
 158
 159
 160
 161
 162
 163
 164
 165
 166
 167
 168
 169
 170
 171
 172
 173
 174
 175
 176
 177
 178
 179
 180
 181
 182
 183
 184
 185
 186
 187
 188
 189
 190
 191
 192
 193
 194
 195
 196
 197
 198
 199
 200
 201
 202
 203
 204
 205
 206
 207
 208
 209
 210
 211
 212
 213
 214
 215
 216
 217
 218
 219
 220
 221
 222
 223
 224
 225
 226
 227
 228
 229
 230
 231
 232
 233
 234
 235
 236
 237
 238
 239
 240
 241
 242
 243
 244
 245
 246
 247
 248
 249
 250
 251
 252
 253
 254
 255
 256
 257
 258
 259
 260
 261
 262
 263
 264
 265
 266
 267
 268
 269
 270
 271
 272
 273
 274
 275
 276
 277
 278
 279
 280
 281
 282
 283
 284
 285
 286
 287
 288
 289
 290
 291
 292
 293
 294
 295
 296
 297
 298
 299
 300
 301
 302
 303
 304
 305
 306
 307
 308
 309
 310
 311
 312
 313
 314
 315
 316
 317
 318
 319
 320
 321
 322
 323
 324
 325
 326
 327
 328
 329
 330
 331
 332
 333
 334
 335
 336
 337
 338
 339
 340
 341
 342
 343
 344
 345
 346
 347
 348
 349
 350
 351
 352
 353
 354
 355
 356
 357
 358
 359
 360
 361
 362
 363
 364
 365
 366
 367
 368
 369
 370
 371
 372
 373
 374
 375
 376
 377
 378
 379
 380
 381
 382
 383
 384
 385
 386
 387
 388
 389
 390
 391
 392
 393
 394
 395
 396
 397
 398
 399
 400
 401
 402
 403
 404
 405
 406
 407
 408
 409
 410
 411
 412
 413
 414
 415
 416
 417
 418
 419
 420
 421
 422
 423
 424
 425
 426
 427
 428
 429
 430
 431
 432
 433
 434
 435
 436
 437
 438
 439
 440
 441
 442
 443
 444
 445
 446
 447
 448
 449
 450
 451
 452
 453
 454
 455
 456
 457
 458
 459
 460
 461
 462
 463
 464
 465
 466
 467
 468
 469
 470
 471
 472
 473
 474
 475
 476
 477
 478
 479
 480
 481
 482
 483
 484
 485
 486
 487
 488
 489
 490
 491
 492
 493
 494
 495
 496
 497
 498
 499
 500
 501
 502
 503
 504
 505
 506
 507
 508
 509
 510
 511
 512
 513
 514
 515
 516
 517
 518
 519
 520
 521
 522
 523
 524
 525
 526
 527
 528
 529
 530
 531
 532
 533
 534
 535
 536
 537
 538
 539
 540
 541
 542
 543
 544
 545
 546
 547
 548
 549
 550
 551
 552
 553
 554
 555
 556
 557
 558
 559
 560
 561
 562
 563
 564
 565
 566
 567
 568
 569
 570
 571
 572
 573
 574
 575
 576
 577
 578
 579
 580
 581
 582
 583
 584
 585
 586
 587
 588
 589
 590
 591
 592
 593
 594
 595
 596
 597
 598
 599
 600
 601
 602
 603
 604
 605
 606
 607
 608
 609
 610
 611
 612
 613
 614
 615
 616
 617
 618
 619
 620
 621
 622
 623
 624
 625
 626
 627
 628
 629
 630
 631
 632
 633
 634
 635
 636
 637
 638
 639
 640
 641
 642
 643
 644
 645
 646
 647
 648
 649
 650
 651
 652
 653
 654
 655
 656
 657
 658
 659
 660
 661
 662
 663
 664
 665
 666
 667
 668
 669
 670
 671
 672
 673
 674
 675
 676
 677
 678
 679
 680
 681
 682
 683
 684
 685
 686
 687
 688
 689
 690
 691
 692
 693
 694
 695
 696
 697
 698
 699
 700
 701
 702
 703
 704
 705
 706
 707
 708
 709
 710
 711
 712
 713
 714
 715
 716
 717
 718
 719
 720
 721
 722
 723
 724
 725
 726
 727
 728
 729
 730
 731
 732
 733
 734
 735
 736
 737
 738
 739
 740
 741
 742
 743
 744
 745
 746
 747
 748
 749
 750
 751
 752
 753
 754
 755
 756
 757
 758
 759
 760
 761
 762
 763
 764
 765
 766
 767
 768
 769
 770
 771
 772
 773
 774
 775
 776
 777
 778
 779
 780
 781
 782
 783
 784
 785
 786
 787
 788
 789
 790
 791
 792
 793
 794
 795
 796
 797
 798
 799
 800
 801
 802
 803
 804
 805
 806
 807
 808
 809
 810
 811
 812
 813
 814
 815
 816
 817
 818
 819
 820
 821
 822
 823
 824
 825
 826
 827
 828
 829
 830
 831
 832
 833
 834
 835
 836
 837
 838
 839
 840
 841
 842
 843
 844
 845
 846
 847
 848
 849
 850
 851
 852
 853
 854
 855
 856
 857
 858
 859
 860
 861
 862
 863
 864
 865
 866
 867
 868
 869
 870
 871
 872
 873
 874
 875
 876
 877
 878
 879
 880
 881
 882
 883
 884
 885
 886
 887
 888
 889
 890
 891
 892
 893
 894
 895
 896
 897
 898
 899
 900
 901
 902
 903
 904
 905
 906
 907
 908
 909
 910
 911
 912
 913
 914
 915
 916
 917
 918
 919
 920
 921
 922
 923
 924
 925
 926
 927
 928
 929
 930
 931
 932
 933
 934
 935
 936
 937
 938
 939
 940
 941
 942
 943
 944
 945
 946
 947
 948
 949
 950
 951
 952
 953
 954
 955
 956
 957
 958
 959
 960
 961
 962
 963
 964
 965
 966
 967
 968
 969
 970
 971
 972
 973
 974
 975
 976
 977
 978
 979
 980
 981
 982
 983
 984
 985
 986
 987
 988
 989
 990
 991
 992
 993
 994
 995
 996
 997
 998
 999
1000
1001
1002
1003
1004
1005
1006
1007
1008
1009
1010
1011
1012
1013
1014
1015
1016
1017
1018
1019
1020
1021
1022
1023
1024
1025
1026
1027
1028
1029
1030
1031
1032
1033
1034
1035
1036
1037
1038
1039
1040
1041
1042
1043
1044
1045
1046
1047
1048
1049
1050
1051
1052
1053
1054
1055
1056
1057
1058
1059
1060
```
| ```
@final
@dataclasses.dataclass(init=False)
class Agent(Generic[AgentDepsT, ResultDataT]):
"""Class for defining "agents" - a way to have a specific type of "conversation" with an LLM.
  Agents are generic in the dependency type they take [`AgentDepsT`][pydantic_ai.tools.AgentDepsT]
  and the result data type they return, [`ResultDataT`][pydantic_ai.result.ResultDataT].
  By default, if neither generic parameter is customised, agents have type `Agent[None, str]`.
  Minimal usage example:
  ```python
  from pydantic_ai import Agent
  agent = Agent('openai:gpt-4o')
  result = agent.run_sync('What is the capital of France?')
  print(result.data)
  #> Paris
  ```
  """
  # we use dataclass fields in order to conveniently know what attributes are available
  model: models.Model | models.KnownModelName | None
"""The default model configured for this agent."""
  name: str | None
"""The name of the agent, used for logging.
  If `None`, we try to infer the agent name from the call frame when the agent is first run.
  """
  end_strategy: EndStrategy
"""Strategy for handling tool calls when a final result is found."""
  model_settings: ModelSettings | None
"""Optional model request settings to use for this agents's runs, by default.
  Note, if `model_settings` is provided by `run`, `run_sync`, or `run_stream`, those settings will
  be merged with this value, with the runtime argument taking priority.
  """
  result_type: type[ResultDataT] = dataclasses.field(repr=False)
"""
  The type of the result data, used to validate the result data, defaults to `str`.
  """
  _deps_type: type[AgentDepsT] = dataclasses.field(repr=False)
  _result_tool_name: str = dataclasses.field(repr=False)
  _result_tool_description: str | None = dataclasses.field(repr=False)
  _result_schema: _result.ResultSchema[ResultDataT] | None = dataclasses.field(repr=False)
  _result_validators: list[_result.ResultValidator[AgentDepsT, ResultDataT]] = dataclasses.field(repr=False)
  _system_prompts: tuple[str, ...] = dataclasses.field(repr=False)
  _system_prompt_functions: list[_system_prompt.SystemPromptRunner[AgentDepsT]] = dataclasses.field(repr=False)
  _system_prompt_dynamic_functions: dict[str, _system_prompt.SystemPromptRunner[AgentDepsT]] = dataclasses.field(
    repr=False
  )
  _function_tools: dict[str, Tool[AgentDepsT]] = dataclasses.field(repr=False)
  _default_retries: int = dataclasses.field(repr=False)
  _max_result_retries: int = dataclasses.field(repr=False)
  _override_deps: _utils.Option[AgentDepsT] = dataclasses.field(default=None, repr=False)
  _override_model: _utils.Option[models.Model] = dataclasses.field(default=None, repr=False)
  def __init__(
    self,
    model: models.Model | models.KnownModelName | None = None,
    *,
    result_type: type[ResultDataT] = str,
    system_prompt: str | Sequence[str] = (),
    deps_type: type[AgentDepsT] = NoneType,
    name: str | None = None,
    model_settings: ModelSettings | None = None,
    retries: int = 1,
    result_tool_name: str = 'final_result',
    result_tool_description: str | None = None,
    result_retries: int | None = None,
    tools: Sequence[Tool[AgentDepsT] | ToolFuncEither[AgentDepsT, ...]] = (),
    defer_model_check: bool = False,
    end_strategy: EndStrategy = 'early',
  ):
"""Create an agent.
    Args:
      model: The default model to use for this agent, if not provide,
        you must provide the model when calling it.
      result_type: The type of the result data, used to validate the result data, defaults to `str`.
      system_prompt: Static system prompts to use for this agent, you can also register system
        prompts via a function with [`system_prompt`][pydantic_ai.Agent.system_prompt].
      deps_type: The type used for dependency injection, this parameter exists solely to allow you to fully
        parameterize the agent, and therefore get the best out of static type checking.
        If you're not using deps, but want type checking to pass, you can set `deps=None` to satisfy Pyright
        or add a type hint `: Agent[None, <return type>]`.
      name: The name of the agent, used for logging. If `None`, we try to infer the agent name from the call frame
        when the agent is first run.
      model_settings: Optional model request settings to use for this agent's runs, by default.
      retries: The default number of retries to allow before raising an error.
      result_tool_name: The name of the tool to use for the final result.
      result_tool_description: The description of the final result tool.
      result_retries: The maximum number of retries to allow for result validation, defaults to `retries`.
      tools: Tools to register with the agent, you can also register tools via the decorators
        [`@agent.tool`][pydantic_ai.Agent.tool] and [`@agent.tool_plain`][pydantic_ai.Agent.tool_plain].
      defer_model_check: by default, if you provide a [named][pydantic_ai.models.KnownModelName] model,
        it's evaluated to create a [`Model`][pydantic_ai.models.Model] instance immediately,
        which checks for the necessary environment variables. Set this to `false`
        to defer the evaluation until the first run. Useful if you want to
        [override the model][pydantic_ai.Agent.override] for testing.
      end_strategy: Strategy for handling tool calls that are requested alongside a final result.
        See [`EndStrategy`][pydantic_ai.agent.EndStrategy] for more information.
    """
    if model is None or defer_model_check:
      self.model = model
    else:
      self.model = models.infer_model(model)
    self.end_strategy = end_strategy
    self.name = name
    self.model_settings = model_settings
    self.result_type = result_type
    self._deps_type = deps_type
    self._result_tool_name = result_tool_name
    self._result_tool_description = result_tool_description
    self._result_schema: _result.ResultSchema[ResultDataT] | None = _result.ResultSchema[result_type].build(
      result_type, result_tool_name, result_tool_description
    )
    self._result_validators: list[_result.ResultValidator[AgentDepsT, ResultDataT]] = []
    self._system_prompts = (system_prompt,) if isinstance(system_prompt, str) else tuple(system_prompt)
    self._system_prompt_functions: list[_system_prompt.SystemPromptRunner[AgentDepsT]] = []
    self._system_prompt_dynamic_functions: dict[str, _system_prompt.SystemPromptRunner[AgentDepsT]] = {}
    self._function_tools: dict[str, Tool[AgentDepsT]] = {}
    self._default_retries = retries
    self._max_result_retries = result_retries if result_retries is not None else retries
    for tool in tools:
      if isinstance(tool, Tool):
        self._register_tool(tool)
      else:
        self._register_tool(Tool(tool))
  @overload
  async def run(
    self,
    user_prompt: str,
    *,
    result_type: None = None,
    message_history: list[_messages.ModelMessage] | None = None,
    model: models.Model | models.KnownModelName | None = None,
    deps: AgentDepsT = None,
    model_settings: ModelSettings | None = None,
    usage_limits: _usage.UsageLimits | None = None,
    usage: _usage.Usage | None = None,
    infer_name: bool = True,
  ) -> result.RunResult[ResultDataT]: ...
  @overload
  async def run(
    self,
    user_prompt: str,
    *,
    result_type: type[RunResultDataT],
    message_history: list[_messages.ModelMessage] | None = None,
    model: models.Model | models.KnownModelName | None = None,
    deps: AgentDepsT = None,
    model_settings: ModelSettings | None = None,
    usage_limits: _usage.UsageLimits | None = None,
    usage: _usage.Usage | None = None,
    infer_name: bool = True,
  ) -> result.RunResult[RunResultDataT]: ...
  async def run(
    self,
    user_prompt: str,
    *,
    message_history: list[_messages.ModelMessage] | None = None,
    model: models.Model | models.KnownModelName | None = None,
    deps: AgentDepsT = None,
    model_settings: ModelSettings | None = None,
    usage_limits: _usage.UsageLimits | None = None,
    usage: _usage.Usage | None = None,
    result_type: type[RunResultDataT] | None = None,
    infer_name: bool = True,
  ) -> result.RunResult[Any]:
"""Run the agent with a user prompt in async mode.
    Example:
```python
    from pydantic_ai import Agent
    agent = Agent('openai:gpt-4o')
    async def main():
      result = await agent.run('What is the capital of France?')
      print(result.data)
      #> Paris
```
    Args:
      result_type: Custom result type to use for this run, `result_type` may only be used if the agent has no
        result validators since result validators would expect an argument that matches the agent's result type.
      user_prompt: User input to start/continue the conversation.
      message_history: History of the conversation so far.
      model: Optional model to use for this run, required if `model` was not set when creating the agent.
      deps: Optional dependencies to use for this run.
      model_settings: Optional settings to use for this model's request.
      usage_limits: Optional limits on model request count or token usage.
      usage: Optional usage to start with, useful for resuming a conversation or agents used in tools.
      infer_name: Whether to try to infer the agent name from the call frame if it's not set.
    Returns:
      The result of the run.
    """
    if infer_name and self.name is None:
      self._infer_name(inspect.currentframe())
    model_used = self._get_model(model)
    deps = self._get_deps(deps)
    new_message_index = len(message_history) if message_history else 0
    result_schema: _result.ResultSchema[RunResultDataT] | None = self._prepare_result_schema(result_type)
    # Build the graph
    graph = self._build_graph(result_type)
    # Build the initial state
    state = _agent_graph.GraphAgentState(
      message_history=message_history[:] if message_history else [],
      usage=usage or _usage.Usage(),
      retries=0,
      run_step=0,
    )
    # We consider it a user error if a user tries to restrict the result type while having a result validator that
    # may change the result type from the restricted type to something else. Therefore, we consider the following
    # typecast reasonable, even though it is possible to violate it with otherwise-type-checked code.
    result_validators = cast(list[_result.ResultValidator[AgentDepsT, RunResultDataT]], self._result_validators)
    # TODO: Instead of this, copy the function tools to ensure they don't share current_retry state between agent
    # runs. Requires some changes to `Tool` to make them copyable though.
    for v in self._function_tools.values():
      v.current_retry = 0
    model_settings = merge_model_settings(self.model_settings, model_settings)
    usage_limits = usage_limits or _usage.UsageLimits()
    with _logfire.span(
      '{agent_name} run {prompt=}',
      prompt=user_prompt,
      agent=self,
      model_name=model_used.model_name if model_used else 'no-model',
      agent_name=self.name or 'agent',
    ) as run_span:
      # Build the deps object for the graph
      graph_deps = _agent_graph.GraphAgentDeps[AgentDepsT, RunResultDataT](
        user_deps=deps,
        prompt=user_prompt,
        new_message_index=new_message_index,
        model=model_used,
        model_settings=model_settings,
        usage_limits=usage_limits,
        max_result_retries=self._max_result_retries,
        end_strategy=self.end_strategy,
        result_schema=result_schema,
        result_tools=self._result_schema.tool_defs() if self._result_schema else [],
        result_validators=result_validators,
        function_tools=self._function_tools,
        run_span=run_span,
      )
      start_node = _agent_graph.UserPromptNode[AgentDepsT](
        user_prompt=user_prompt,
        system_prompts=self._system_prompts,
        system_prompt_functions=self._system_prompt_functions,
        system_prompt_dynamic_functions=self._system_prompt_dynamic_functions,
      )
      # Actually run
      end_result, _ = await graph.run(
        start_node,
        state=state,
        deps=graph_deps,
        infer_name=False,
      )
    # Build final run result
    # We don't do any advanced checking if the data is actually from a final result or not
    return result.RunResult(
      state.message_history,
      new_message_index,
      end_result.data,
      end_result.tool_name,
      state.usage,
    )
  @overload
  def run_sync(
    self,
    user_prompt: str,
    *,
    message_history: list[_messages.ModelMessage] | None = None,
    model: models.Model | models.KnownModelName | None = None,
    deps: AgentDepsT = None,
    model_settings: ModelSettings | None = None,
    usage_limits: _usage.UsageLimits | None = None,
    usage: _usage.Usage | None = None,
    infer_name: bool = True,
  ) -> result.RunResult[ResultDataT]: ...
  @overload
  def run_sync(
    self,
    user_prompt: str,
    *,
    result_type: type[RunResultDataT] | None,
    message_history: list[_messages.ModelMessage] | None = None,
    model: models.Model | models.KnownModelName | None = None,
    deps: AgentDepsT = None,
    model_settings: ModelSettings | None = None,
    usage_limits: _usage.UsageLimits | None = None,
    usage: _usage.Usage | None = None,
    infer_name: bool = True,
  ) -> result.RunResult[RunResultDataT]: ...
  def run_sync(
    self,
    user_prompt: str,
    *,
    result_type: type[RunResultDataT] | None = None,
    message_history: list[_messages.ModelMessage] | None = None,
    model: models.Model | models.KnownModelName | None = None,
    deps: AgentDepsT = None,
    model_settings: ModelSettings | None = None,
    usage_limits: _usage.UsageLimits | None = None,
    usage: _usage.Usage | None = None,
    infer_name: bool = True,
  ) -> result.RunResult[Any]:
"""Run the agent with a user prompt synchronously.
    This is a convenience method that wraps [`self.run`][pydantic_ai.Agent.run] with `loop.run_until_complete(...)`.
    You therefore can't use this method inside async code or if there's an active event loop.
    Example:
```python
    from pydantic_ai import Agent
    agent = Agent('openai:gpt-4o')
    result_sync = agent.run_sync('What is the capital of Italy?')
    print(result_sync.data)
    #> Rome
```
    Args:
      result_type: Custom result type to use for this run, `result_type` may only be used if the agent has no
        result validators since result validators would expect an argument that matches the agent's result type.
      user_prompt: User input to start/continue the conversation.
      message_history: History of the conversation so far.
      model: Optional model to use for this run, required if `model` was not set when creating the agent.
      deps: Optional dependencies to use for this run.
      model_settings: Optional settings to use for this model's request.
      usage_limits: Optional limits on model request count or token usage.
      usage: Optional usage to start with, useful for resuming a conversation or agents used in tools.
      infer_name: Whether to try to infer the agent name from the call frame if it's not set.
    Returns:
      The result of the run.
    """
    if infer_name and self.name is None:
      self._infer_name(inspect.currentframe())
    return asyncio.get_event_loop().run_until_complete(
      self.run(
        user_prompt,
        result_type=result_type,
        message_history=message_history,
        model=model,
        deps=deps,
        model_settings=model_settings,
        usage_limits=usage_limits,
        usage=usage,
        infer_name=False,
      )
    )
  @overload
  def run_stream(
    self,
    user_prompt: str,
    *,
    result_type: None = None,
    message_history: list[_messages.ModelMessage] | None = None,
    model: models.Model | models.KnownModelName | None = None,
    deps: AgentDepsT = None,
    model_settings: ModelSettings | None = None,
    usage_limits: _usage.UsageLimits | None = None,
    usage: _usage.Usage | None = None,
    infer_name: bool = True,
  ) -> AbstractAsyncContextManager[result.StreamedRunResult[AgentDepsT, ResultDataT]]: ...
  @overload
  def run_stream(
    self,
    user_prompt: str,
    *,
    result_type: type[RunResultDataT],
    message_history: list[_messages.ModelMessage] | None = None,
    model: models.Model | models.KnownModelName | None = None,
    deps: AgentDepsT = None,
    model_settings: ModelSettings | None = None,
    usage_limits: _usage.UsageLimits | None = None,
    usage: _usage.Usage | None = None,
    infer_name: bool = True,
  ) -> AbstractAsyncContextManager[result.StreamedRunResult[AgentDepsT, RunResultDataT]]: ...
  @asynccontextmanager
  async def run_stream(
    self,
    user_prompt: str,
    *,
    result_type: type[RunResultDataT] | None = None,
    message_history: list[_messages.ModelMessage] | None = None,
    model: models.Model | models.KnownModelName | None = None,
    deps: AgentDepsT = None,
    model_settings: ModelSettings | None = None,
    usage_limits: _usage.UsageLimits | None = None,
    usage: _usage.Usage | None = None,
    infer_name: bool = True,
  ) -> AsyncIterator[result.StreamedRunResult[AgentDepsT, Any]]:
"""Run the agent with a user prompt in async mode, returning a streamed response.
    Example:
```python
    from pydantic_ai import Agent
    agent = Agent('openai:gpt-4o')
    async def main():
      async with agent.run_stream('What is the capital of the UK?') as response:
        print(await response.get_data())
        #> London
```
    Args:
      result_type: Custom result type to use for this run, `result_type` may only be used if the agent has no
        result validators since result validators would expect an argument that matches the agent's result type.
      user_prompt: User input to start/continue the conversation.
      message_history: History of the conversation so far.
      model: Optional model to use for this run, required if `model` was not set when creating the agent.
      deps: Optional dependencies to use for this run.
      model_settings: Optional settings to use for this model's request.
      usage_limits: Optional limits on model request count or token usage.
      usage: Optional usage to start with, useful for resuming a conversation or agents used in tools.
      infer_name: Whether to try to infer the agent name from the call frame if it's not set.
    Returns:
      The result of the run.
    """
    if infer_name and self.name is None:
      # f_back because `asynccontextmanager` adds one frame
      if frame := inspect.currentframe(): # pragma: no branch
        self._infer_name(frame.f_back)
    model_used = self._get_model(model)
    deps = self._get_deps(deps)
    new_message_index = len(message_history) if message_history else 0
    result_schema: _result.ResultSchema[RunResultDataT] | None = self._prepare_result_schema(result_type)
    # Build the graph
    graph = self._build_stream_graph(result_type)
    # Build the initial state
    graph_state = _agent_graph.GraphAgentState(
      message_history=message_history[:] if message_history else [],
      usage=usage or _usage.Usage(),
      retries=0,
      run_step=0,
    )
    # We consider it a user error if a user tries to restrict the result type while having a result validator that
    # may change the result type from the restricted type to something else. Therefore, we consider the following
    # typecast reasonable, even though it is possible to violate it with otherwise-type-checked code.
    result_validators = cast(list[_result.ResultValidator[AgentDepsT, RunResultDataT]], self._result_validators)
    # TODO: Instead of this, copy the function tools to ensure they don't share current_retry state between agent
    # runs. Requires some changes to `Tool` to make them copyable though.
    for v in self._function_tools.values():
      v.current_retry = 0
    model_settings = merge_model_settings(self.model_settings, model_settings)
    usage_limits = usage_limits or _usage.UsageLimits()
    with _logfire.span(
      '{agent_name} run stream {prompt=}',
      prompt=user_prompt,
      agent=self,
      model_name=model_used.model_name if model_used else 'no-model',
      agent_name=self.name or 'agent',
    ) as run_span:
      # Build the deps object for the graph
      graph_deps = _agent_graph.GraphAgentDeps[AgentDepsT, RunResultDataT](
        user_deps=deps,
        prompt=user_prompt,
        new_message_index=new_message_index,
        model=model_used,
        model_settings=model_settings,
        usage_limits=usage_limits,
        max_result_retries=self._max_result_retries,
        end_strategy=self.end_strategy,
        result_schema=result_schema,
        result_tools=self._result_schema.tool_defs() if self._result_schema else [],
        result_validators=result_validators,
        function_tools=self._function_tools,
        run_span=run_span,
      )
      start_node = _agent_graph.StreamUserPromptNode[AgentDepsT](
        user_prompt=user_prompt,
        system_prompts=self._system_prompts,
        system_prompt_functions=self._system_prompt_functions,
        system_prompt_dynamic_functions=self._system_prompt_dynamic_functions,
      )
      # Actually run
      node = start_node
      history: list[HistoryStep[_agent_graph.GraphAgentState, RunResultDataT]] = []
      while True:
        if isinstance(node, _agent_graph.StreamModelRequestNode):
          node = cast(
            _agent_graph.StreamModelRequestNode[
              AgentDepsT, result.StreamedRunResult[AgentDepsT, RunResultDataT]
            ],
            node,
          )
          async with node.run_to_result(GraphRunContext(graph_state, graph_deps)) as r:
            if isinstance(r, End):
              yield r.data
              break
        assert not isinstance(node, End) # the previous line should be hit first
        node = await graph.next(
          node,
          history,
          state=graph_state,
          deps=graph_deps,
          infer_name=False,
        )
  @contextmanager
  def override(
    self,
    *,
    deps: AgentDepsT | _utils.Unset = _utils.UNSET,
    model: models.Model | models.KnownModelName | _utils.Unset = _utils.UNSET,
  ) -> Iterator[None]:
"""Context manager to temporarily override agent dependencies and model.
    This is particularly useful when testing.
    You can find an example of this [here](../testing-evals.md#overriding-model-via-pytest-fixtures).
    Args:
      deps: The dependencies to use instead of the dependencies passed to the agent run.
      model: The model to use instead of the model passed to the agent run.
    """
    if _utils.is_set(deps):
      override_deps_before = self._override_deps
      self._override_deps = _utils.Some(deps)
    else:
      override_deps_before = _utils.UNSET
    # noinspection PyTypeChecker
    if _utils.is_set(model):
      override_model_before = self._override_model
      # noinspection PyTypeChecker
      self._override_model = _utils.Some(models.infer_model(model)) # pyright: ignore[reportArgumentType]
    else:
      override_model_before = _utils.UNSET
    try:
      yield
    finally:
      if _utils.is_set(override_deps_before):
        self._override_deps = override_deps_before
      if _utils.is_set(override_model_before):
        self._override_model = override_model_before
  @overload
  def system_prompt(
    self, func: Callable[[RunContext[AgentDepsT]], str], /
  ) -> Callable[[RunContext[AgentDepsT]], str]: ...
  @overload
  def system_prompt(
    self, func: Callable[[RunContext[AgentDepsT]], Awaitable[str]], /
  ) -> Callable[[RunContext[AgentDepsT]], Awaitable[str]]: ...
  @overload
  def system_prompt(self, func: Callable[[], str], /) -> Callable[[], str]: ...
  @overload
  def system_prompt(self, func: Callable[[], Awaitable[str]], /) -> Callable[[], Awaitable[str]]: ...
  @overload
  def system_prompt(
    self, /, *, dynamic: bool = False
  ) -> Callable[[_system_prompt.SystemPromptFunc[AgentDepsT]], _system_prompt.SystemPromptFunc[AgentDepsT]]: ...
  def system_prompt(
    self,
    func: _system_prompt.SystemPromptFunc[AgentDepsT] | None = None,
    /,
    *,
    dynamic: bool = False,
  ) -> (
    Callable[[_system_prompt.SystemPromptFunc[AgentDepsT]], _system_prompt.SystemPromptFunc[AgentDepsT]]
    | _system_prompt.SystemPromptFunc[AgentDepsT]
  ):
"""Decorator to register a system prompt function.
    Optionally takes [`RunContext`][pydantic_ai.tools.RunContext] as its only argument.
    Can decorate a sync or async functions.
    The decorator can be used either bare (`agent.system_prompt`) or as a function call
    (`agent.system_prompt(...)`), see the examples below.
    Overloads for every possible signature of `system_prompt` are included so the decorator doesn't obscure
    the type of the function, see `tests/typed_agent.py` for tests.
    Args:
      func: The function to decorate
      dynamic: If True, the system prompt will be reevaluated even when `messages_history` is provided,
        see [`SystemPromptPart.dynamic_ref`][pydantic_ai.messages.SystemPromptPart.dynamic_ref]
    Example:
```python
    from pydantic_ai import Agent, RunContext
    agent = Agent('test', deps_type=str)
    @agent.system_prompt
    def simple_system_prompt() -> str:
      return 'foobar'
    @agent.system_prompt(dynamic=True)
    async def async_system_prompt(ctx: RunContext[str]) -> str:
      return f'{ctx.deps} is the best'
```
    """
    if func is None:
      def decorator(
        func_: _system_prompt.SystemPromptFunc[AgentDepsT],
      ) -> _system_prompt.SystemPromptFunc[AgentDepsT]:
        runner = _system_prompt.SystemPromptRunner[AgentDepsT](func_, dynamic=dynamic)
        self._system_prompt_functions.append(runner)
        if dynamic:
          self._system_prompt_dynamic_functions[func_.__qualname__] = runner
        return func_
      return decorator
    else:
      assert not dynamic, "dynamic can't be True in this case"
      self._system_prompt_functions.append(_system_prompt.SystemPromptRunner[AgentDepsT](func, dynamic=dynamic))
      return func
  @overload
  def result_validator(
    self, func: Callable[[RunContext[AgentDepsT], ResultDataT], ResultDataT], /
  ) -> Callable[[RunContext[AgentDepsT], ResultDataT], ResultDataT]: ...
  @overload
  def result_validator(
    self, func: Callable[[RunContext[AgentDepsT], ResultDataT], Awaitable[ResultDataT]], /
  ) -> Callable[[RunContext[AgentDepsT], ResultDataT], Awaitable[ResultDataT]]: ...
  @overload
  def result_validator(
    self, func: Callable[[ResultDataT], ResultDataT], /
  ) -> Callable[[ResultDataT], ResultDataT]: ...
  @overload
  def result_validator(
    self, func: Callable[[ResultDataT], Awaitable[ResultDataT]], /
  ) -> Callable[[ResultDataT], Awaitable[ResultDataT]]: ...
  def result_validator(
    self, func: _result.ResultValidatorFunc[AgentDepsT, ResultDataT], /
  ) -> _result.ResultValidatorFunc[AgentDepsT, ResultDataT]:
"""Decorator to register a result validator function.
    Optionally takes [`RunContext`][pydantic_ai.tools.RunContext] as its first argument.
    Can decorate a sync or async functions.
    Overloads for every possible signature of `result_validator` are included so the decorator doesn't obscure
    the type of the function, see `tests/typed_agent.py` for tests.
    Example:
```python
    from pydantic_ai import Agent, ModelRetry, RunContext
    agent = Agent('test', deps_type=str)
    @agent.result_validator
    def result_validator_simple(data: str) -> str:
      if 'wrong' in data:
        raise ModelRetry('wrong response')
      return data
    @agent.result_validator
    async def result_validator_deps(ctx: RunContext[str], data: str) -> str:
      if ctx.deps in data:
        raise ModelRetry('wrong response')
      return data
    result = agent.run_sync('foobar', deps='spam')
    print(result.data)
    #> success (no tool calls)
```
    """
    self._result_validators.append(_result.ResultValidator[AgentDepsT, Any](func))
    return func
  @overload
  def tool(self, func: ToolFuncContext[AgentDepsT, ToolParams], /) -> ToolFuncContext[AgentDepsT, ToolParams]: ...
  @overload
  def tool(
    self,
    /,
    *,
    retries: int | None = None,
    prepare: ToolPrepareFunc[AgentDepsT] | None = None,
    docstring_format: DocstringFormat = 'auto',
    require_parameter_descriptions: bool = False,
  ) -> Callable[[ToolFuncContext[AgentDepsT, ToolParams]], ToolFuncContext[AgentDepsT, ToolParams]]: ...
  def tool(
    self,
    func: ToolFuncContext[AgentDepsT, ToolParams] | None = None,
    /,
    *,
    retries: int | None = None,
    prepare: ToolPrepareFunc[AgentDepsT] | None = None,
    docstring_format: DocstringFormat = 'auto',
    require_parameter_descriptions: bool = False,
  ) -> Any:
"""Decorator to register a tool function which takes [`RunContext`][pydantic_ai.tools.RunContext] as its first argument.
    Can decorate a sync or async functions.
    The docstring is inspected to extract both the tool description and description of each parameter,
    [learn more](../tools.md#function-tools-and-schema).
    We can't add overloads for every possible signature of tool, since the return type is a recursive union
    so the signature of functions decorated with `@agent.tool` is obscured.
    Example:
```python
    from pydantic_ai import Agent, RunContext
    agent = Agent('test', deps_type=int)
    @agent.tool
    def foobar(ctx: RunContext[int], x: int) -> int:
      return ctx.deps + x
    @agent.tool(retries=2)
    async def spam(ctx: RunContext[str], y: float) -> float:
      return ctx.deps + y
    result = agent.run_sync('foobar', deps=1)
    print(result.data)
    #> {"foobar":1,"spam":1.0}
```
    Args:
      func: The tool function to register.
      retries: The number of retries to allow for this tool, defaults to the agent's default retries,
        which defaults to 1.
      prepare: custom method to prepare the tool definition for each step, return `None` to omit this
        tool from a given step. This is useful if you want to customise a tool at call time,
        or omit it completely from a step. See [`ToolPrepareFunc`][pydantic_ai.tools.ToolPrepareFunc].
      docstring_format: The format of the docstring, see [`DocstringFormat`][pydantic_ai.tools.DocstringFormat].
        Defaults to `'auto'`, such that the format is inferred from the structure of the docstring.
      require_parameter_descriptions: If True, raise an error if a parameter description is missing. Defaults to False.
    """
    if func is None:
      def tool_decorator(
        func_: ToolFuncContext[AgentDepsT, ToolParams],
      ) -> ToolFuncContext[AgentDepsT, ToolParams]:
        # noinspection PyTypeChecker
        self._register_function(func_, True, retries, prepare, docstring_format, require_parameter_descriptions)
        return func_
      return tool_decorator
    else:
      # noinspection PyTypeChecker
      self._register_function(func, True, retries, prepare, docstring_format, require_parameter_descriptions)
      return func
  @overload
  def tool_plain(self, func: ToolFuncPlain[ToolParams], /) -> ToolFuncPlain[ToolParams]: ...
  @overload
  def tool_plain(
    self,
    /,
    *,
    retries: int | None = None,
    prepare: ToolPrepareFunc[AgentDepsT] | None = None,
    docstring_format: DocstringFormat = 'auto',
    require_parameter_descriptions: bool = False,
  ) -> Callable[[ToolFuncPlain[ToolParams]], ToolFuncPlain[ToolParams]]: ...
  def tool_plain(
    self,
    func: ToolFuncPlain[ToolParams] | None = None,
    /,
    *,
    retries: int | None = None,
    prepare: ToolPrepareFunc[AgentDepsT] | None = None,
    docstring_format: DocstringFormat = 'auto',
    require_parameter_descriptions: bool = False,
  ) -> Any:
"""Decorator to register a tool function which DOES NOT take `RunContext` as an argument.
    Can decorate a sync or async functions.
    The docstring is inspected to extract both the tool description and description of each parameter,
    [learn more](../tools.md#function-tools-and-schema).
    We can't add overloads for every possible signature of tool, since the return type is a recursive union
    so the signature of functions decorated with `@agent.tool` is obscured.
    Example:
```python
    from pydantic_ai import Agent, RunContext
    agent = Agent('test')
    @agent.tool
    def foobar(ctx: RunContext[int]) -> int:
      return 123
    @agent.tool(retries=2)
    async def spam(ctx: RunContext[str]) -> float:
      return 3.14
    result = agent.run_sync('foobar', deps=1)
    print(result.data)
    #> {"foobar":123,"spam":3.14}
```
    Args:
      func: The tool function to register.
      retries: The number of retries to allow for this tool, defaults to the agent's default retries,
        which defaults to 1.
      prepare: custom method to prepare the tool definition for each step, return `None` to omit this
        tool from a given step. This is useful if you want to customise a tool at call time,
        or omit it completely from a step. See [`ToolPrepareFunc`][pydantic_ai.tools.ToolPrepareFunc].
      docstring_format: The format of the docstring, see [`DocstringFormat`][pydantic_ai.tools.DocstringFormat].
        Defaults to `'auto'`, such that the format is inferred from the structure of the docstring.
      require_parameter_descriptions: If True, raise an error if a parameter description is missing. Defaults to False.
    """
    if func is None:
      def tool_decorator(func_: ToolFuncPlain[ToolParams]) -> ToolFuncPlain[ToolParams]:
        # noinspection PyTypeChecker
        self._register_function(
          func_, False, retries, prepare, docstring_format, require_parameter_descriptions
        )
        return func_
      return tool_decorator
    else:
      self._register_function(func, False, retries, prepare, docstring_format, require_parameter_descriptions)
      return func
  def _register_function(
    self,
    func: ToolFuncEither[AgentDepsT, ToolParams],
    takes_ctx: bool,
    retries: int | None,
    prepare: ToolPrepareFunc[AgentDepsT] | None,
    docstring_format: DocstringFormat,
    require_parameter_descriptions: bool,
  ) -> None:
"""Private utility to register a function as a tool."""
    retries_ = retries if retries is not None else self._default_retries
    tool = Tool[AgentDepsT](
      func,
      takes_ctx=takes_ctx,
      max_retries=retries_,
      prepare=prepare,
      docstring_format=docstring_format,
      require_parameter_descriptions=require_parameter_descriptions,
    )
    self._register_tool(tool)
  def _register_tool(self, tool: Tool[AgentDepsT]) -> None:
"""Private utility to register a tool instance."""
    if tool.max_retries is None:
      # noinspection PyTypeChecker
      tool = dataclasses.replace(tool, max_retries=self._default_retries)
    if tool.name in self._function_tools:
      raise exceptions.UserError(f'Tool name conflicts with existing tool: {tool.name!r}')
    if self._result_schema and tool.name in self._result_schema.tools:
      raise exceptions.UserError(f'Tool name conflicts with result schema name: {tool.name!r}')
    self._function_tools[tool.name] = tool
  def _get_model(self, model: models.Model | models.KnownModelName | None) -> models.Model:
"""Create a model configured for this agent.
    Args:
      model: model to use for this run, required if `model` was not set when creating the agent.
    Returns:
      The model used
    """
    model_: models.Model
    if some_model := self._override_model:
      # we don't want `override()` to cover up errors from the model not being defined, hence this check
      if model is None and self.model is None:
        raise exceptions.UserError(
          '`model` must be set either when creating the agent or when calling it. '
          '(Even when `override(model=...)` is customizing the model that will actually be called)'
        )
      model_ = some_model.value
    elif model is not None:
      model_ = models.infer_model(model)
    elif self.model is not None:
      # noinspection PyTypeChecker
      model_ = self.model = models.infer_model(self.model)
    else:
      raise exceptions.UserError('`model` must be set either when creating the agent or when calling it.')
    return model_
  def _get_deps(self: Agent[T, ResultDataT], deps: T) -> T:
"""Get deps for a run.
    If we've overridden deps via `_override_deps`, use that, otherwise use the deps passed to the call.
    We could do runtime type checking of deps against `self._deps_type`, but that's a slippery slope.
    """
    if some_deps := self._override_deps:
      return some_deps.value
    else:
      return deps
  def _infer_name(self, function_frame: FrameType | None) -> None:
"""Infer the agent name from the call frame.
    Usage should be `self._infer_name(inspect.currentframe())`.
    """
    assert self.name is None, 'Name already set'
    if function_frame is not None: # pragma: no branch
      if parent_frame := function_frame.f_back: # pragma: no branch
        for name, item in parent_frame.f_locals.items():
          if item is self:
            self.name = name
            return
        if parent_frame.f_locals != parent_frame.f_globals:
          # if we couldn't find the agent in locals and globals are a different dict, try globals
          for name, item in parent_frame.f_globals.items():
            if item is self:
              self.name = name
              return
  @property
  @deprecated(
    'The `last_run_messages` attribute has been removed, use `capture_run_messages` instead.', category=None
  )
  def last_run_messages(self) -> list[_messages.ModelMessage]:
    raise AttributeError('The `last_run_messages` attribute has been removed, use `capture_run_messages` instead.')
  def _build_graph(
    self, result_type: type[RunResultDataT] | None
  ) -> Graph[_agent_graph.GraphAgentState, _agent_graph.GraphAgentDeps[AgentDepsT, Any], Any]:
    return _agent_graph.build_agent_graph(self.name, self._deps_type, result_type or self.result_type)
  def _build_stream_graph(
    self, result_type: type[RunResultDataT] | None
  ) -> Graph[_agent_graph.GraphAgentState, _agent_graph.GraphAgentDeps[AgentDepsT, Any], Any]:
    return _agent_graph.build_agent_stream_graph(self.name, self._deps_type, result_type or self.result_type)
  def _prepare_result_schema(
    self, result_type: type[RunResultDataT] | None
  ) -> _result.ResultSchema[RunResultDataT] | None:
    if result_type is not None:
      if self._result_validators:
        raise exceptions.UserError('Cannot set a custom run `result_type` when the agent has result validators')
      return _result.ResultSchema[result_type].build(
        result_type, self._result_tool_name, self._result_tool_description
      )
    else:
      return self._result_schema # pyright: ignore[reportReturnType]

```
  
---|---  
####  model `instance-attribute`
```
model: Model | KnownModelName | None

```

The default model configured for this agent.
####  __init__
```
__init__(
  model: Model | KnownModelName | None = None,
  *,
  result_type: type[ResultDataT] = str,
  system_prompt: str | Sequence[str] = (),
  deps_type: type[AgentDepsT] = NoneType,
  name: str | None = None,
  model_settings: ModelSettings | None = None,
  retries: int = 1,
  result_tool_name: str = "final_result",
  result_tool_description: str | None = None,
  result_retries: int | None = None,
  tools: Sequence[
    Tool[AgentDepsT] | ToolFuncEither[AgentDepsT, ...]
  ] = (),
  defer_model_check: bool = False,
  end_strategy: EndStrategy = "early"
)

```

Create an agent.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`model` |  `Model | KnownModelName | None` |  The default model to use for this agent, if not provide, you must provide the model when calling it. |  `None`  
`result_type` |  `type[ResultDataT]` |  The type of the result data, used to validate the result data, defaults to `str`. |  `str`  
`system_prompt` |  `str | Sequence[str]` |  Static system prompts to use for this agent, you can also register system prompts via a function with `system_prompt`. |  `()`  
`deps_type` |  `type[AgentDepsT]` |  The type used for dependency injection, this parameter exists solely to allow you to fully parameterize the agent, and therefore get the best out of static type checking. If you're not using deps, but want type checking to pass, you can set `deps=None` to satisfy Pyright or add a type hint `: Agent[None, <return type>]`. |  `NoneType`  
`name` |  `str | None` |  The name of the agent, used for logging. If `None`, we try to infer the agent name from the call frame when the agent is first run. |  `None`  
`model_settings` |  `ModelSettings | None` |  Optional model request settings to use for this agent's runs, by default. |  `None`  
`retries` |  `int` |  The default number of retries to allow before raising an error. |  `1`  
`result_tool_name` |  `str` |  The name of the tool to use for the final result. |  `'final_result'`  
`result_tool_description` |  `str | None` |  The description of the final result tool. |  `None`  
`result_retries` |  `int | None` |  The maximum number of retries to allow for result validation, defaults to `retries`. |  `None`  
`tools` |  `Sequence[Tool[AgentDepsT] | ToolFuncEither[AgentDepsT, ...]]` |  Tools to register with the agent, you can also register tools via the decorators `@agent.tool` and `@agent.tool_plain`. |  `()`  
`defer_model_check` |  `bool` |  by default, if you provide a named model, it's evaluated to create a `Model` instance immediately, which checks for the necessary environment variables. Set this to `false` to defer the evaluation until the first run. Useful if you want to override the model for testing. |  `False`  
`end_strategy` |  `EndStrategy` |  Strategy for handling tool calls that are requested alongside a final result. See `EndStrategy` for more information. |  `'early'`  
Source code in `pydantic_ai_slim/pydantic_ai/agent.py`
```
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
```
| ```
def __init__(
  self,
  model: models.Model | models.KnownModelName | None = None,
  *,
  result_type: type[ResultDataT] = str,
  system_prompt: str | Sequence[str] = (),
  deps_type: type[AgentDepsT] = NoneType,
  name: str | None = None,
  model_settings: ModelSettings | None = None,
  retries: int = 1,
  result_tool_name: str = 'final_result',
  result_tool_description: str | None = None,
  result_retries: int | None = None,
  tools: Sequence[Tool[AgentDepsT] | ToolFuncEither[AgentDepsT, ...]] = (),
  defer_model_check: bool = False,
  end_strategy: EndStrategy = 'early',
):
"""Create an agent.
  Args:
    model: The default model to use for this agent, if not provide,
      you must provide the model when calling it.
    result_type: The type of the result data, used to validate the result data, defaults to `str`.
    system_prompt: Static system prompts to use for this agent, you can also register system
      prompts via a function with [`system_prompt`][pydantic_ai.Agent.system_prompt].
    deps_type: The type used for dependency injection, this parameter exists solely to allow you to fully
      parameterize the agent, and therefore get the best out of static type checking.
      If you're not using deps, but want type checking to pass, you can set `deps=None` to satisfy Pyright
      or add a type hint `: Agent[None, <return type>]`.
    name: The name of the agent, used for logging. If `None`, we try to infer the agent name from the call frame
      when the agent is first run.
    model_settings: Optional model request settings to use for this agent's runs, by default.
    retries: The default number of retries to allow before raising an error.
    result_tool_name: The name of the tool to use for the final result.
    result_tool_description: The description of the final result tool.
    result_retries: The maximum number of retries to allow for result validation, defaults to `retries`.
    tools: Tools to register with the agent, you can also register tools via the decorators
      [`@agent.tool`][pydantic_ai.Agent.tool] and [`@agent.tool_plain`][pydantic_ai.Agent.tool_plain].
    defer_model_check: by default, if you provide a [named][pydantic_ai.models.KnownModelName] model,
      it's evaluated to create a [`Model`][pydantic_ai.models.Model] instance immediately,
      which checks for the necessary environment variables. Set this to `false`
      to defer the evaluation until the first run. Useful if you want to
      [override the model][pydantic_ai.Agent.override] for testing.
    end_strategy: Strategy for handling tool calls that are requested alongside a final result.
      See [`EndStrategy`][pydantic_ai.agent.EndStrategy] for more information.
  """
  if model is None or defer_model_check:
    self.model = model
  else:
    self.model = models.infer_model(model)
  self.end_strategy = end_strategy
  self.name = name
  self.model_settings = model_settings
  self.result_type = result_type
  self._deps_type = deps_type
  self._result_tool_name = result_tool_name
  self._result_tool_description = result_tool_description
  self._result_schema: _result.ResultSchema[ResultDataT] | None = _result.ResultSchema[result_type].build(
    result_type, result_tool_name, result_tool_description
  )
  self._result_validators: list[_result.ResultValidator[AgentDepsT, ResultDataT]] = []
  self._system_prompts = (system_prompt,) if isinstance(system_prompt, str) else tuple(system_prompt)
  self._system_prompt_functions: list[_system_prompt.SystemPromptRunner[AgentDepsT]] = []
  self._system_prompt_dynamic_functions: dict[str, _system_prompt.SystemPromptRunner[AgentDepsT]] = {}
  self._function_tools: dict[str, Tool[AgentDepsT]] = {}
  self._default_retries = retries
  self._max_result_retries = result_retries if result_retries is not None else retries
  for tool in tools:
    if isinstance(tool, Tool):
      self._register_tool(tool)
    else:
      self._register_tool(Tool(tool))

```
  
---|---  
####  end_strategy `instance-attribute`
```
end_strategy: EndStrategy = end_strategy

```

Strategy for handling tool calls when a final result is found.
####  name `instance-attribute`
```
name: str | None = name

```

The name of the agent, used for logging.
If `None`, we try to infer the agent name from the call frame when the agent is first run.
####  model_settings `instance-attribute`
```
model_settings: ModelSettings | None = model_settings

```

Optional model request settings to use for this agents's runs, by default.
Note, if `model_settings` is provided by `run`, `run_sync`, or `run_stream`, those settings will be merged with this value, with the runtime argument taking priority.
####  result_type `class-attribute` `instance-attribute`
```
result_type: type[ResultDataT] = result_type

```

The type of the result data, used to validate the result data, defaults to `str`.
####  run `async`
```
run(
  user_prompt: str,
  *,
  result_type: None = None,
  message_history: list[ModelMessage] | None = None,
  model: Model | KnownModelName | None = None,
  deps: AgentDepsT = None,
  model_settings: ModelSettings | None = None,
  usage_limits: UsageLimits | None = None,
  usage: Usage | None = None,
  infer_name: bool = True
) -> RunResult[ResultDataT]

```

```
run(
  user_prompt: str,
  *,
  result_type: type[RunResultDataT],
  message_history: list[ModelMessage] | None = None,
  model: Model | KnownModelName | None = None,
  deps: AgentDepsT = None,
  model_settings: ModelSettings | None = None,
  usage_limits: UsageLimits | None = None,
  usage: Usage | None = None,
  infer_name: bool = True
) -> RunResult[RunResultDataT]

```

```
run(
  user_prompt: str,
  *,
  message_history: list[ModelMessage] | None = None,
  model: Model | KnownModelName | None = None,
  deps: AgentDepsT = None,
  model_settings: ModelSettings | None = None,
  usage_limits: UsageLimits | None = None,
  usage: Usage | None = None,
  result_type: type[RunResultDataT] | None = None,
  infer_name: bool = True
) -> RunResult[Any]

```

Run the agent with a user prompt in async mode.
Example: 
```
from pydantic_ai import Agent
agent = Agent('openai:gpt-4o')
async def main():
  result = await agent.run('What is the capital of France?')
  print(result.data)
  #> Paris

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`result_type` |  `type[RunResultDataT] | None` |  Custom result type to use for this run, `result_type` may only be used if the agent has no result validators since result validators would expect an argument that matches the agent's result type. |  `None`  
`user_prompt` |  `str` |  User input to start/continue the conversation. |  _required_  
`message_history` |  `list[ModelMessage] | None` |  History of the conversation so far. |  `None`  
`model` |  `Model | KnownModelName | None` |  Optional model to use for this run, required if `model` was not set when creating the agent. |  `None`  
`deps` |  `AgentDepsT` |  Optional dependencies to use for this run. |  `None`  
`model_settings` |  `ModelSettings | None` |  Optional settings to use for this model's request. |  `None`  
`usage_limits` |  `UsageLimits | None` |  Optional limits on model request count or token usage. |  `None`  
`usage` |  `Usage | None` |  Optional usage to start with, useful for resuming a conversation or agents used in tools. |  `None`  
`infer_name` |  `bool` |  Whether to try to infer the agent name from the call frame if it's not set. |  `True`  
Returns:
Type | Description  
---|---  
`RunResult[Any]` |  The result of the run.  
Source code in `pydantic_ai_slim/pydantic_ai/agent.py`
```
234
235
236
237
238
239
240
241
242
243
244
245
246
247
248
249
250
251
252
253
254
255
256
257
258
259
260
261
262
263
264
265
266
267
268
269
270
271
272
273
274
275
276
277
278
279
280
281
282
283
284
285
286
287
288
289
290
291
292
293
294
295
296
297
298
299
300
301
302
303
304
305
306
307
308
309
310
311
312
313
314
315
316
317
318
319
320
321
322
323
324
325
326
327
328
329
330
331
332
333
334
335
336
337
338
339
340
341
342
343
344
345
346
347
348
349
350
351
352
353
354
355
```
| ```
async def run(
  self,
  user_prompt: str,
  *,
  message_history: list[_messages.ModelMessage] | None = None,
  model: models.Model | models.KnownModelName | None = None,
  deps: AgentDepsT = None,
  model_settings: ModelSettings | None = None,
  usage_limits: _usage.UsageLimits | None = None,
  usage: _usage.Usage | None = None,
  result_type: type[RunResultDataT] | None = None,
  infer_name: bool = True,
) -> result.RunResult[Any]:
"""Run the agent with a user prompt in async mode.
  Example:
  ```python
  from pydantic_ai import Agent
  agent = Agent('openai:gpt-4o')
  async def main():
    result = await agent.run('What is the capital of France?')
    print(result.data)
    #> Paris
  ```
  Args:
    result_type: Custom result type to use for this run, `result_type` may only be used if the agent has no
      result validators since result validators would expect an argument that matches the agent's result type.
    user_prompt: User input to start/continue the conversation.
    message_history: History of the conversation so far.
    model: Optional model to use for this run, required if `model` was not set when creating the agent.
    deps: Optional dependencies to use for this run.
    model_settings: Optional settings to use for this model's request.
    usage_limits: Optional limits on model request count or token usage.
    usage: Optional usage to start with, useful for resuming a conversation or agents used in tools.
    infer_name: Whether to try to infer the agent name from the call frame if it's not set.
  Returns:
    The result of the run.
  """
  if infer_name and self.name is None:
    self._infer_name(inspect.currentframe())
  model_used = self._get_model(model)
  deps = self._get_deps(deps)
  new_message_index = len(message_history) if message_history else 0
  result_schema: _result.ResultSchema[RunResultDataT] | None = self._prepare_result_schema(result_type)
  # Build the graph
  graph = self._build_graph(result_type)
  # Build the initial state
  state = _agent_graph.GraphAgentState(
    message_history=message_history[:] if message_history else [],
    usage=usage or _usage.Usage(),
    retries=0,
    run_step=0,
  )
  # We consider it a user error if a user tries to restrict the result type while having a result validator that
  # may change the result type from the restricted type to something else. Therefore, we consider the following
  # typecast reasonable, even though it is possible to violate it with otherwise-type-checked code.
  result_validators = cast(list[_result.ResultValidator[AgentDepsT, RunResultDataT]], self._result_validators)
  # TODO: Instead of this, copy the function tools to ensure they don't share current_retry state between agent
  # runs. Requires some changes to `Tool` to make them copyable though.
  for v in self._function_tools.values():
    v.current_retry = 0
  model_settings = merge_model_settings(self.model_settings, model_settings)
  usage_limits = usage_limits or _usage.UsageLimits()
  with _logfire.span(
    '{agent_name} run {prompt=}',
    prompt=user_prompt,
    agent=self,
    model_name=model_used.model_name if model_used else 'no-model',
    agent_name=self.name or 'agent',
  ) as run_span:
    # Build the deps object for the graph
    graph_deps = _agent_graph.GraphAgentDeps[AgentDepsT, RunResultDataT](
      user_deps=deps,
      prompt=user_prompt,
      new_message_index=new_message_index,
      model=model_used,
      model_settings=model_settings,
      usage_limits=usage_limits,
      max_result_retries=self._max_result_retries,
      end_strategy=self.end_strategy,
      result_schema=result_schema,
      result_tools=self._result_schema.tool_defs() if self._result_schema else [],
      result_validators=result_validators,
      function_tools=self._function_tools,
      run_span=run_span,
    )
    start_node = _agent_graph.UserPromptNode[AgentDepsT](
      user_prompt=user_prompt,
      system_prompts=self._system_prompts,
      system_prompt_functions=self._system_prompt_functions,
      system_prompt_dynamic_functions=self._system_prompt_dynamic_functions,
    )
    # Actually run
    end_result, _ = await graph.run(
      start_node,
      state=state,
      deps=graph_deps,
      infer_name=False,
    )
  # Build final run result
  # We don't do any advanced checking if the data is actually from a final result or not
  return result.RunResult(
    state.message_history,
    new_message_index,
    end_result.data,
    end_result.tool_name,
    state.usage,
  )

```
  
---|---  
####  run_sync
```
run_sync(
  user_prompt: str,
  *,
  message_history: list[ModelMessage] | None = None,
  model: Model | KnownModelName | None = None,
  deps: AgentDepsT = None,
  model_settings: ModelSettings | None = None,
  usage_limits: UsageLimits | None = None,
  usage: Usage | None = None,
  infer_name: bool = True
) -> RunResult[ResultDataT]

```

```
run_sync(
  user_prompt: str,
  *,
  result_type: type[RunResultDataT] | None,
  message_history: list[ModelMessage] | None = None,
  model: Model | KnownModelName | None = None,
  deps: AgentDepsT = None,
  model_settings: ModelSettings | None = None,
  usage_limits: UsageLimits | None = None,
  usage: Usage | None = None,
  infer_name: bool = True
) -> RunResult[RunResultDataT]

```

```
run_sync(
  user_prompt: str,
  *,
  result_type: type[RunResultDataT] | None = None,
  message_history: list[ModelMessage] | None = None,
  model: Model | KnownModelName | None = None,
  deps: AgentDepsT = None,
  model_settings: ModelSettings | None = None,
  usage_limits: UsageLimits | None = None,
  usage: Usage | None = None,
  infer_name: bool = True
) -> RunResult[Any]

```

Run the agent with a user prompt synchronously.
This is a convenience method that wraps `self.run` with `loop.run_until_complete(...)`. You therefore can't use this method inside async code or if there's an active event loop.
Example: 
```
from pydantic_ai import Agent
agent = Agent('openai:gpt-4o')
result_sync = agent.run_sync('What is the capital of Italy?')
print(result_sync.data)
#> Rome

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`result_type` |  `type[RunResultDataT] | None` |  Custom result type to use for this run, `result_type` may only be used if the agent has no result validators since result validators would expect an argument that matches the agent's result type. |  `None`  
`user_prompt` |  `str` |  User input to start/continue the conversation. |  _required_  
`message_history` |  `list[ModelMessage] | None` |  History of the conversation so far. |  `None`  
`model` |  `Model | KnownModelName | None` |  Optional model to use for this run, required if `model` was not set when creating the agent. |  `None`  
`deps` |  `AgentDepsT` |  Optional dependencies to use for this run. |  `None`  
`model_settings` |  `ModelSettings | None` |  Optional settings to use for this model's request. |  `None`  
`usage_limits` |  `UsageLimits | None` |  Optional limits on model request count or token usage. |  `None`  
`usage` |  `Usage | None` |  Optional usage to start with, useful for resuming a conversation or agents used in tools. |  `None`  
`infer_name` |  `bool` |  Whether to try to infer the agent name from the call frame if it's not set. |  `True`  
Returns:
Type | Description  
---|---  
`RunResult[Any]` |  The result of the run.  
Source code in `pydantic_ai_slim/pydantic_ai/agent.py`
```
386
387
388
389
390
391
392
393
394
395
396
397
398
399
400
401
402
403
404
405
406
407
408
409
410
411
412
413
414
415
416
417
418
419
420
421
422
423
424
425
426
427
428
429
430
431
432
433
434
435
436
437
438
439
440
441
442
443
444
```
| ```
def run_sync(
  self,
  user_prompt: str,
  *,
  result_type: type[RunResultDataT] | None = None,
  message_history: list[_messages.ModelMessage] | None = None,
  model: models.Model | models.KnownModelName | None = None,
  deps: AgentDepsT = None,
  model_settings: ModelSettings | None = None,
  usage_limits: _usage.UsageLimits | None = None,
  usage: _usage.Usage | None = None,
  infer_name: bool = True,
) -> result.RunResult[Any]:
"""Run the agent with a user prompt synchronously.
  This is a convenience method that wraps [`self.run`][pydantic_ai.Agent.run] with `loop.run_until_complete(...)`.
  You therefore can't use this method inside async code or if there's an active event loop.
  Example:
  ```python
  from pydantic_ai import Agent
  agent = Agent('openai:gpt-4o')
  result_sync = agent.run_sync('What is the capital of Italy?')
  print(result_sync.data)
  #> Rome
  ```
  Args:
    result_type: Custom result type to use for this run, `result_type` may only be used if the agent has no
      result validators since result validators would expect an argument that matches the agent's result type.
    user_prompt: User input to start/continue the conversation.
    message_history: History of the conversation so far.
    model: Optional model to use for this run, required if `model` was not set when creating the agent.
    deps: Optional dependencies to use for this run.
    model_settings: Optional settings to use for this model's request.
    usage_limits: Optional limits on model request count or token usage.
    usage: Optional usage to start with, useful for resuming a conversation or agents used in tools.
    infer_name: Whether to try to infer the agent name from the call frame if it's not set.
  Returns:
    The result of the run.
  """
  if infer_name and self.name is None:
    self._infer_name(inspect.currentframe())
  return asyncio.get_event_loop().run_until_complete(
    self.run(
      user_prompt,
      result_type=result_type,
      message_history=message_history,
      model=model,
      deps=deps,
      model_settings=model_settings,
      usage_limits=usage_limits,
      usage=usage,
      infer_name=False,
    )
  )

```
  
---|---  
####  run_stream `async`
```
run_stream(
  user_prompt: str,
  *,
  result_type: None = None,
  message_history: list[ModelMessage] | None = None,
  model: Model | KnownModelName | None = None,
  deps: AgentDepsT = None,
  model_settings: ModelSettings | None = None,
  usage_limits: UsageLimits | None = None,
  usage: Usage | None = None,
  infer_name: bool = True
) -> AbstractAsyncContextManager[
  StreamedRunResult[AgentDepsT, ResultDataT]
]

```

```
run_stream(
  user_prompt: str,
  *,
  result_type: type[RunResultDataT],
  message_history: list[ModelMessage] | None = None,
  model: Model | KnownModelName | None = None,
  deps: AgentDepsT = None,
  model_settings: ModelSettings | None = None,
  usage_limits: UsageLimits | None = None,
  usage: Usage | None = None,
  infer_name: bool = True
) -> AbstractAsyncContextManager[
  StreamedRunResult[AgentDepsT, RunResultDataT]
]

```

```
run_stream(
  user_prompt: str,
  *,
  result_type: type[RunResultDataT] | None = None,
  message_history: list[ModelMessage] | None = None,
  model: Model | KnownModelName | None = None,
  deps: AgentDepsT = None,
  model_settings: ModelSettings | None = None,
  usage_limits: UsageLimits | None = None,
  usage: Usage | None = None,
  infer_name: bool = True
) -> AsyncIterator[StreamedRunResult[AgentDepsT, Any]]

```

Run the agent with a user prompt in async mode, returning a streamed response.
Example: 
```
from pydantic_ai import Agent
agent = Agent('openai:gpt-4o')
async def main():
  async with agent.run_stream('What is the capital of the UK?') as response:
    print(await response.get_data())
    #> London

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`result_type` |  `type[RunResultDataT] | None` |  Custom result type to use for this run, `result_type` may only be used if the agent has no result validators since result validators would expect an argument that matches the agent's result type. |  `None`  
`user_prompt` |  `str` |  User input to start/continue the conversation. |  _required_  
`message_history` |  `list[ModelMessage] | None` |  History of the conversation so far. |  `None`  
`model` |  `Model | KnownModelName | None` |  Optional model to use for this run, required if `model` was not set when creating the agent. |  `None`  
`deps` |  `AgentDepsT` |  Optional dependencies to use for this run. |  `None`  
`model_settings` |  `ModelSettings | None` |  Optional settings to use for this model's request. |  `None`  
`usage_limits` |  `UsageLimits | None` |  Optional limits on model request count or token usage. |  `None`  
`usage` |  `Usage | None` |  Optional usage to start with, useful for resuming a conversation or agents used in tools. |  `None`  
`infer_name` |  `bool` |  Whether to try to infer the agent name from the call frame if it's not set. |  `True`  
Returns:
Type | Description  
---|---  
`AsyncIterator[StreamedRunResult[AgentDepsT, Any]]` |  The result of the run.  
Source code in `pydantic_ai_slim/pydantic_ai/agent.py`
```
476
477
478
479
480
481
482
483
484
485
486
487
488
489
490
491
492
493
494
495
496
497
498
499
500
501
502
503
504
505
506
507
508
509
510
511
512
513
514
515
516
517
518
519
520
521
522
523
524
525
526
527
528
529
530
531
532
533
534
535
536
537
538
539
540
541
542
543
544
545
546
547
548
549
550
551
552
553
554
555
556
557
558
559
560
561
562
563
564
565
566
567
568
569
570
571
572
573
574
575
576
577
578
579
580
581
582
583
584
585
586
587
588
589
590
591
592
593
594
595
596
597
598
599
600
601
602
603
604
605
606
```
| ```
@asynccontextmanager
async def run_stream(
  self,
  user_prompt: str,
  *,
  result_type: type[RunResultDataT] | None = None,
  message_history: list[_messages.ModelMessage] | None = None,
  model: models.Model | models.KnownModelName | None = None,
  deps: AgentDepsT = None,
  model_settings: ModelSettings | None = None,
  usage_limits: _usage.UsageLimits | None = None,
  usage: _usage.Usage | None = None,
  infer_name: bool = True,
) -> AsyncIterator[result.StreamedRunResult[AgentDepsT, Any]]:
"""Run the agent with a user prompt in async mode, returning a streamed response.
  Example:
  ```python
  from pydantic_ai import Agent
  agent = Agent('openai:gpt-4o')
  async def main():
    async with agent.run_stream('What is the capital of the UK?') as response:
      print(await response.get_data())
      #> London
  ```
  Args:
    result_type: Custom result type to use for this run, `result_type` may only be used if the agent has no
      result validators since result validators would expect an argument that matches the agent's result type.
    user_prompt: User input to start/continue the conversation.
    message_history: History of the conversation so far.
    model: Optional model to use for this run, required if `model` was not set when creating the agent.
    deps: Optional dependencies to use for this run.
    model_settings: Optional settings to use for this model's request.
    usage_limits: Optional limits on model request count or token usage.
    usage: Optional usage to start with, useful for resuming a conversation or agents used in tools.
    infer_name: Whether to try to infer the agent name from the call frame if it's not set.
  Returns:
    The result of the run.
  """
  if infer_name and self.name is None:
    # f_back because `asynccontextmanager` adds one frame
    if frame := inspect.currentframe(): # pragma: no branch
      self._infer_name(frame.f_back)
  model_used = self._get_model(model)
  deps = self._get_deps(deps)
  new_message_index = len(message_history) if message_history else 0
  result_schema: _result.ResultSchema[RunResultDataT] | None = self._prepare_result_schema(result_type)
  # Build the graph
  graph = self._build_stream_graph(result_type)
  # Build the initial state
  graph_state = _agent_graph.GraphAgentState(
    message_history=message_history[:] if message_history else [],
    usage=usage or _usage.Usage(),
    retries=0,
    run_step=0,
  )
  # We consider it a user error if a user tries to restrict the result type while having a result validator that
  # may change the result type from the restricted type to something else. Therefore, we consider the following
  # typecast reasonable, even though it is possible to violate it with otherwise-type-checked code.
  result_validators = cast(list[_result.ResultValidator[AgentDepsT, RunResultDataT]], self._result_validators)
  # TODO: Instead of this, copy the function tools to ensure they don't share current_retry state between agent
  # runs. Requires some changes to `Tool` to make them copyable though.
  for v in self._function_tools.values():
    v.current_retry = 0
  model_settings = merge_model_settings(self.model_settings, model_settings)
  usage_limits = usage_limits or _usage.UsageLimits()
  with _logfire.span(
    '{agent_name} run stream {prompt=}',
    prompt=user_prompt,
    agent=self,
    model_name=model_used.model_name if model_used else 'no-model',
    agent_name=self.name or 'agent',
  ) as run_span:
    # Build the deps object for the graph
    graph_deps = _agent_graph.GraphAgentDeps[AgentDepsT, RunResultDataT](
      user_deps=deps,
      prompt=user_prompt,
      new_message_index=new_message_index,
      model=model_used,
      model_settings=model_settings,
      usage_limits=usage_limits,
      max_result_retries=self._max_result_retries,
      end_strategy=self.end_strategy,
      result_schema=result_schema,
      result_tools=self._result_schema.tool_defs() if self._result_schema else [],
      result_validators=result_validators,
      function_tools=self._function_tools,
      run_span=run_span,
    )
    start_node = _agent_graph.StreamUserPromptNode[AgentDepsT](
      user_prompt=user_prompt,
      system_prompts=self._system_prompts,
      system_prompt_functions=self._system_prompt_functions,
      system_prompt_dynamic_functions=self._system_prompt_dynamic_functions,
    )
    # Actually run
    node = start_node
    history: list[HistoryStep[_agent_graph.GraphAgentState, RunResultDataT]] = []
    while True:
      if isinstance(node, _agent_graph.StreamModelRequestNode):
        node = cast(
          _agent_graph.StreamModelRequestNode[
            AgentDepsT, result.StreamedRunResult[AgentDepsT, RunResultDataT]
          ],
          node,
        )
        async with node.run_to_result(GraphRunContext(graph_state, graph_deps)) as r:
          if isinstance(r, End):
            yield r.data
            break
      assert not isinstance(node, End) # the previous line should be hit first
      node = await graph.next(
        node,
        history,
        state=graph_state,
        deps=graph_deps,
        infer_name=False,
      )

```
  
---|---  
####  override
```
override(
  *,
  deps: AgentDepsT | Unset = UNSET,
  model: Model | KnownModelName | Unset = UNSET
) -> Iterator[None]

```

Context manager to temporarily override agent dependencies and model.
This is particularly useful when testing. You can find an example of this here.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`deps` |  `AgentDepsT | Unset` |  The dependencies to use instead of the dependencies passed to the agent run. |  `UNSET`  
`model` |  `Model | KnownModelName | Unset` |  The model to use instead of the model passed to the agent run. |  `UNSET`  
Source code in `pydantic_ai_slim/pydantic_ai/agent.py`
```
608
609
610
611
612
613
614
615
616
617
618
619
620
621
622
623
624
625
626
627
628
629
630
631
632
633
634
635
636
637
638
639
640
641
642
643
644
```
| ```
@contextmanager
def override(
  self,
  *,
  deps: AgentDepsT | _utils.Unset = _utils.UNSET,
  model: models.Model | models.KnownModelName | _utils.Unset = _utils.UNSET,
) -> Iterator[None]:
"""Context manager to temporarily override agent dependencies and model.
  This is particularly useful when testing.
  You can find an example of this [here](../testing-evals.md#overriding-model-via-pytest-fixtures).
  Args:
    deps: The dependencies to use instead of the dependencies passed to the agent run.
    model: The model to use instead of the model passed to the agent run.
  """
  if _utils.is_set(deps):
    override_deps_before = self._override_deps
    self._override_deps = _utils.Some(deps)
  else:
    override_deps_before = _utils.UNSET
  # noinspection PyTypeChecker
  if _utils.is_set(model):
    override_model_before = self._override_model
    # noinspection PyTypeChecker
    self._override_model = _utils.Some(models.infer_model(model)) # pyright: ignore[reportArgumentType]
  else:
    override_model_before = _utils.UNSET
  try:
    yield
  finally:
    if _utils.is_set(override_deps_before):
      self._override_deps = override_deps_before
    if _utils.is_set(override_model_before):
      self._override_model = override_model_before

```
  
---|---  
####  system_prompt
```
system_prompt(
  func: Callable[[RunContext[AgentDepsT]], str]
) -> Callable[[RunContext[AgentDepsT]], str]

```

```
system_prompt(
  func: Callable[[RunContext[AgentDepsT]], Awaitable[str]]
) -> Callable[[RunContext[AgentDepsT]], Awaitable[str]]

```

```
system_prompt(func: Callable[[], str]) -> Callable[[], str]

```

```
system_prompt(
  func: Callable[[], Awaitable[str]]
) -> Callable[[], Awaitable[str]]

```

```
system_prompt(*, dynamic: bool = False) -> Callable[
  [SystemPromptFunc[AgentDepsT]],
  SystemPromptFunc[AgentDepsT],
]

```

```
system_prompt(
  func: SystemPromptFunc[AgentDepsT] | None = None,
  /,
  *,
  dynamic: bool = False,
) -> (
  Callable[
    [SystemPromptFunc[AgentDepsT]],
    SystemPromptFunc[AgentDepsT],
  ]
  | SystemPromptFunc[AgentDepsT]
)

```

Decorator to register a system prompt function.
Optionally takes `RunContext` as its only argument. Can decorate a sync or async functions.
The decorator can be used either bare (`agent.system_prompt`) or as a function call (`agent.system_prompt(...)`), see the examples below.
Overloads for every possible signature of `system_prompt` are included so the decorator doesn't obscure the type of the function, see `tests/typed_agent.py` for tests.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`func` |  `SystemPromptFunc[AgentDepsT] | None` |  The function to decorate |  `None`  
`dynamic` |  `bool` |  If True, the system prompt will be reevaluated even when `messages_history` is provided, see `SystemPromptPart.dynamic_ref` |  `False`  
Example: 
```
from pydantic_ai import Agent, RunContext
agent = Agent('test', deps_type=str)
@agent.system_prompt
def simple_system_prompt() -> str:
  return 'foobar'
@agent.system_prompt(dynamic=True)
async def async_system_prompt(ctx: RunContext[str]) -> str:
  return f'{ctx.deps} is the best'

```

Source code in `pydantic_ai_slim/pydantic_ai/agent.py`
```
667
668
669
670
671
672
673
674
675
676
677
678
679
680
681
682
683
684
685
686
687
688
689
690
691
692
693
694
695
696
697
698
699
700
701
702
703
704
705
706
707
708
709
710
711
712
713
714
715
716
717
718
719
720
721
722
723
```
| ```
def system_prompt(
  self,
  func: _system_prompt.SystemPromptFunc[AgentDepsT] | None = None,
  /,
  *,
  dynamic: bool = False,
) -> (
  Callable[[_system_prompt.SystemPromptFunc[AgentDepsT]], _system_prompt.SystemPromptFunc[AgentDepsT]]
  | _system_prompt.SystemPromptFunc[AgentDepsT]
):
"""Decorator to register a system prompt function.
  Optionally takes [`RunContext`][pydantic_ai.tools.RunContext] as its only argument.
  Can decorate a sync or async functions.
  The decorator can be used either bare (`agent.system_prompt`) or as a function call
  (`agent.system_prompt(...)`), see the examples below.
  Overloads for every possible signature of `system_prompt` are included so the decorator doesn't obscure
  the type of the function, see `tests/typed_agent.py` for tests.
  Args:
    func: The function to decorate
    dynamic: If True, the system prompt will be reevaluated even when `messages_history` is provided,
      see [`SystemPromptPart.dynamic_ref`][pydantic_ai.messages.SystemPromptPart.dynamic_ref]
  Example:
  ```python
  from pydantic_ai import Agent, RunContext
  agent = Agent('test', deps_type=str)
  @agent.system_prompt
  def simple_system_prompt() -> str:
    return 'foobar'
  @agent.system_prompt(dynamic=True)
  async def async_system_prompt(ctx: RunContext[str]) -> str:
    return f'{ctx.deps} is the best'
  ```
  """
  if func is None:
    def decorator(
      func_: _system_prompt.SystemPromptFunc[AgentDepsT],
    ) -> _system_prompt.SystemPromptFunc[AgentDepsT]:
      runner = _system_prompt.SystemPromptRunner[AgentDepsT](func_, dynamic=dynamic)
      self._system_prompt_functions.append(runner)
      if dynamic:
        self._system_prompt_dynamic_functions[func_.__qualname__] = runner
      return func_
    return decorator
  else:
    assert not dynamic, "dynamic can't be True in this case"
    self._system_prompt_functions.append(_system_prompt.SystemPromptRunner[AgentDepsT](func, dynamic=dynamic))
    return func

```
  
---|---  
####  result_validator
```
result_validator(
  func: Callable[
    [RunContext[AgentDepsT], ResultDataT], ResultDataT
  ]
) -> Callable[
  [RunContext[AgentDepsT], ResultDataT], ResultDataT
]

```

```
result_validator(
  func: Callable[
    [RunContext[AgentDepsT], ResultDataT],
    Awaitable[ResultDataT],
  ]
) -> Callable[
  [RunContext[AgentDepsT], ResultDataT],
  Awaitable[ResultDataT],
]

```

```
result_validator(
  func: Callable[[ResultDataT], ResultDataT]
) -> Callable[[ResultDataT], ResultDataT]

```

```
result_validator(
  func: Callable[[ResultDataT], Awaitable[ResultDataT]]
) -> Callable[[ResultDataT], Awaitable[ResultDataT]]

```

```
result_validator(
  func: ResultValidatorFunc[AgentDepsT, ResultDataT]
) -> ResultValidatorFunc[AgentDepsT, ResultDataT]

```

Decorator to register a result validator function.
Optionally takes `RunContext` as its first argument. Can decorate a sync or async functions.
Overloads for every possible signature of `result_validator` are included so the decorator doesn't obscure the type of the function, see `tests/typed_agent.py` for tests.
Example: 
```
from pydantic_ai import Agent, ModelRetry, RunContext
agent = Agent('test', deps_type=str)
@agent.result_validator
def result_validator_simple(data: str) -> str:
  if 'wrong' in data:
    raise ModelRetry('wrong response')
  return data
@agent.result_validator
async def result_validator_deps(ctx: RunContext[str], data: str) -> str:
  if ctx.deps in data:
    raise ModelRetry('wrong response')
  return data
result = agent.run_sync('foobar', deps='spam')
print(result.data)
#> success (no tool calls)

```

Source code in `pydantic_ai_slim/pydantic_ai/agent.py`
```
745
746
747
748
749
750
751
752
753
754
755
756
757
758
759
760
761
762
763
764
765
766
767
768
769
770
771
772
773
774
775
776
777
778
779
780
```
| ```
def result_validator(
  self, func: _result.ResultValidatorFunc[AgentDepsT, ResultDataT], /
) -> _result.ResultValidatorFunc[AgentDepsT, ResultDataT]:
"""Decorator to register a result validator function.
  Optionally takes [`RunContext`][pydantic_ai.tools.RunContext] as its first argument.
  Can decorate a sync or async functions.
  Overloads for every possible signature of `result_validator` are included so the decorator doesn't obscure
  the type of the function, see `tests/typed_agent.py` for tests.
  Example:
  ```python
  from pydantic_ai import Agent, ModelRetry, RunContext
  agent = Agent('test', deps_type=str)
  @agent.result_validator
  def result_validator_simple(data: str) -> str:
    if 'wrong' in data:
      raise ModelRetry('wrong response')
    return data
  @agent.result_validator
  async def result_validator_deps(ctx: RunContext[str], data: str) -> str:
    if ctx.deps in data:
      raise ModelRetry('wrong response')
    return data
  result = agent.run_sync('foobar', deps='spam')
  print(result.data)
  #> success (no tool calls)
  ```
  """
  self._result_validators.append(_result.ResultValidator[AgentDepsT, Any](func))
  return func

```
  
---|---  
####  tool
```
tool(
  func: ToolFuncContext[AgentDepsT, ToolParams]
) -> ToolFuncContext[AgentDepsT, ToolParams]

```

```
tool(
  *,
  retries: int | None = None,
  prepare: ToolPrepareFunc[AgentDepsT] | None = None,
  docstring_format: DocstringFormat = "auto",
  require_parameter_descriptions: bool = False
) -> Callable[
  [ToolFuncContext[AgentDepsT, ToolParams]],
  ToolFuncContext[AgentDepsT, ToolParams],
]

```

```
tool(
  func: (
    ToolFuncContext[AgentDepsT, ToolParams] | None
  ) = None,
  /,
  *,
  retries: int | None = None,
  prepare: ToolPrepareFunc[AgentDepsT] | None = None,
  docstring_format: DocstringFormat = "auto",
  require_parameter_descriptions: bool = False,
) -> Any

```

Decorator to register a tool function which takes `RunContext` as its first argument.
Can decorate a sync or async functions.
The docstring is inspected to extract both the tool description and description of each parameter, learn more.
We can't add overloads for every possible signature of tool, since the return type is a recursive union so the signature of functions decorated with `@agent.tool` is obscured.
Example: 
```
from pydantic_ai import Agent, RunContext
agent = Agent('test', deps_type=int)
@agent.tool
def foobar(ctx: RunContext[int], x: int) -> int:
  return ctx.deps + x
@agent.tool(retries=2)
async def spam(ctx: RunContext[str], y: float) -> float:
  return ctx.deps + y
result = agent.run_sync('foobar', deps=1)
print(result.data)
#> {"foobar":1,"spam":1.0}

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`func` |  `ToolFuncContext[AgentDepsT, ToolParams] | None` |  The tool function to register. |  `None`  
`retries` |  `int | None` |  The number of retries to allow for this tool, defaults to the agent's default retries, which defaults to 1. |  `None`  
`prepare` |  `ToolPrepareFunc[AgentDepsT] | None` |  custom method to prepare the tool definition for each step, return `None` to omit this tool from a given step. This is useful if you want to customise a tool at call time, or omit it completely from a step. See `ToolPrepareFunc`. |  `None`  
`docstring_format` |  `DocstringFormat` |  The format of the docstring, see `DocstringFormat`. Defaults to `'auto'`, such that the format is inferred from the structure of the docstring. |  `'auto'`  
`require_parameter_descriptions` |  `bool` |  If True, raise an error if a parameter description is missing. Defaults to False. |  `False`  
Source code in `pydantic_ai_slim/pydantic_ai/agent.py`
```
796
797
798
799
800
801
802
803
804
805
806
807
808
809
810
811
812
813
814
815
816
817
818
819
820
821
822
823
824
825
826
827
828
829
830
831
832
833
834
835
836
837
838
839
840
841
842
843
844
845
846
847
848
849
850
851
852
853
854
855
856
857
858
859
```
| ```
def tool(
  self,
  func: ToolFuncContext[AgentDepsT, ToolParams] | None = None,
  /,
  *,
  retries: int | None = None,
  prepare: ToolPrepareFunc[AgentDepsT] | None = None,
  docstring_format: DocstringFormat = 'auto',
  require_parameter_descriptions: bool = False,
) -> Any:
"""Decorator to register a tool function which takes [`RunContext`][pydantic_ai.tools.RunContext] as its first argument.
  Can decorate a sync or async functions.
  The docstring is inspected to extract both the tool description and description of each parameter,
  [learn more](../tools.md#function-tools-and-schema).
  We can't add overloads for every possible signature of tool, since the return type is a recursive union
  so the signature of functions decorated with `@agent.tool` is obscured.
  Example:
  ```python
  from pydantic_ai import Agent, RunContext
  agent = Agent('test', deps_type=int)
  @agent.tool
  def foobar(ctx: RunContext[int], x: int) -> int:
    return ctx.deps + x
  @agent.tool(retries=2)
  async def spam(ctx: RunContext[str], y: float) -> float:
    return ctx.deps + y
  result = agent.run_sync('foobar', deps=1)
  print(result.data)
  #> {"foobar":1,"spam":1.0}
  ```
  Args:
    func: The tool function to register.
    retries: The number of retries to allow for this tool, defaults to the agent's default retries,
      which defaults to 1.
    prepare: custom method to prepare the tool definition for each step, return `None` to omit this
      tool from a given step. This is useful if you want to customise a tool at call time,
      or omit it completely from a step. See [`ToolPrepareFunc`][pydantic_ai.tools.ToolPrepareFunc].
    docstring_format: The format of the docstring, see [`DocstringFormat`][pydantic_ai.tools.DocstringFormat].
      Defaults to `'auto'`, such that the format is inferred from the structure of the docstring.
    require_parameter_descriptions: If True, raise an error if a parameter description is missing. Defaults to False.
  """
  if func is None:
    def tool_decorator(
      func_: ToolFuncContext[AgentDepsT, ToolParams],
    ) -> ToolFuncContext[AgentDepsT, ToolParams]:
      # noinspection PyTypeChecker
      self._register_function(func_, True, retries, prepare, docstring_format, require_parameter_descriptions)
      return func_
    return tool_decorator
  else:
    # noinspection PyTypeChecker
    self._register_function(func, True, retries, prepare, docstring_format, require_parameter_descriptions)
    return func

```
  
---|---  
####  tool_plain
```
tool_plain(
  func: ToolFuncPlain[ToolParams],
) -> ToolFuncPlain[ToolParams]

```

```
tool_plain(
  *,
  retries: int | None = None,
  prepare: ToolPrepareFunc[AgentDepsT] | None = None,
  docstring_format: DocstringFormat = "auto",
  require_parameter_descriptions: bool = False
) -> Callable[
  [ToolFuncPlain[ToolParams]], ToolFuncPlain[ToolParams]
]

```

```
tool_plain(
  func: ToolFuncPlain[ToolParams] | None = None,
  /,
  *,
  retries: int | None = None,
  prepare: ToolPrepareFunc[AgentDepsT] | None = None,
  docstring_format: DocstringFormat = "auto",
  require_parameter_descriptions: bool = False,
) -> Any

```

Decorator to register a tool function which DOES NOT take `RunContext` as an argument.
Can decorate a sync or async functions.
The docstring is inspected to extract both the tool description and description of each parameter, learn more.
We can't add overloads for every possible signature of tool, since the return type is a recursive union so the signature of functions decorated with `@agent.tool` is obscured.
Example: 
```
from pydantic_ai import Agent, RunContext
agent = Agent('test')
@agent.tool
def foobar(ctx: RunContext[int]) -> int:
  return 123
@agent.tool(retries=2)
async def spam(ctx: RunContext[str]) -> float:
  return 3.14
result = agent.run_sync('foobar', deps=1)
print(result.data)
#> {"foobar":123,"spam":3.14}

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`func` |  `ToolFuncPlain[ToolParams] | None` |  The tool function to register. |  `None`  
`retries` |  `int | None` |  The number of retries to allow for this tool, defaults to the agent's default retries, which defaults to 1. |  `None`  
`prepare` |  `ToolPrepareFunc[AgentDepsT] | None` |  custom method to prepare the tool definition for each step, return `None` to omit this tool from a given step. This is useful if you want to customise a tool at call time, or omit it completely from a step. See `ToolPrepareFunc`. |  `None`  
`docstring_format` |  `DocstringFormat` |  The format of the docstring, see `DocstringFormat`. Defaults to `'auto'`, such that the format is inferred from the structure of the docstring. |  `'auto'`  
`require_parameter_descriptions` |  `bool` |  If True, raise an error if a parameter description is missing. Defaults to False. |  `False`  
Source code in `pydantic_ai_slim/pydantic_ai/agent.py`
```
875
876
877
878
879
880
881
882
883
884
885
886
887
888
889
890
891
892
893
894
895
896
897
898
899
900
901
902
903
904
905
906
907
908
909
910
911
912
913
914
915
916
917
918
919
920
921
922
923
924
925
926
927
928
929
930
931
932
933
934
935
936
937
```
| ```
def tool_plain(
  self,
  func: ToolFuncPlain[ToolParams] | None = None,
  /,
  *,
  retries: int | None = None,
  prepare: ToolPrepareFunc[AgentDepsT] | None = None,
  docstring_format: DocstringFormat = 'auto',
  require_parameter_descriptions: bool = False,
) -> Any:
"""Decorator to register a tool function which DOES NOT take `RunContext` as an argument.
  Can decorate a sync or async functions.
  The docstring is inspected to extract both the tool description and description of each parameter,
  [learn more](../tools.md#function-tools-and-schema).
  We can't add overloads for every possible signature of tool, since the return type is a recursive union
  so the signature of functions decorated with `@agent.tool` is obscured.
  Example:
  ```python
  from pydantic_ai import Agent, RunContext
  agent = Agent('test')
  @agent.tool
  def foobar(ctx: RunContext[int]) -> int:
    return 123
  @agent.tool(retries=2)
  async def spam(ctx: RunContext[str]) -> float:
    return 3.14
  result = agent.run_sync('foobar', deps=1)
  print(result.data)
  #> {"foobar":123,"spam":3.14}
  ```
  Args:
    func: The tool function to register.
    retries: The number of retries to allow for this tool, defaults to the agent's default retries,
      which defaults to 1.
    prepare: custom method to prepare the tool definition for each step, return `None` to omit this
      tool from a given step. This is useful if you want to customise a tool at call time,
      or omit it completely from a step. See [`ToolPrepareFunc`][pydantic_ai.tools.ToolPrepareFunc].
    docstring_format: The format of the docstring, see [`DocstringFormat`][pydantic_ai.tools.DocstringFormat].
      Defaults to `'auto'`, such that the format is inferred from the structure of the docstring.
    require_parameter_descriptions: If True, raise an error if a parameter description is missing. Defaults to False.
  """
  if func is None:
    def tool_decorator(func_: ToolFuncPlain[ToolParams]) -> ToolFuncPlain[ToolParams]:
      # noinspection PyTypeChecker
      self._register_function(
        func_, False, retries, prepare, docstring_format, require_parameter_descriptions
      )
      return func_
    return tool_decorator
  else:
    self._register_function(func, False, retries, prepare, docstring_format, require_parameter_descriptions)
    return func

```
  
---|---  
###  EndStrategy `module-attribute`
```
EndStrategy = Literal['early', 'exhaustive']

```

The strategy for handling multiple tool calls when a final result is found.
  * `'early'`: Stop processing other tool calls once a final result is found
  * `'exhaustive'`: Process all tool calls even after finding a final result


###  capture_run_messages
```
capture_run_messages() -> Iterator[list[ModelMessage]]

```

Context manager to access the messages used in a `run`, `run_sync`, or `run_stream` call.
Useful when a run may raise an exception, see model errors for more information.
Examples: 
```
from pydantic_ai import Agent, capture_run_messages
agent = Agent('test')
with capture_run_messages() as messages:
  try:
    result = agent.run_sync('foobar')
  except Exception:
    print(messages)
    raise

```

Note
If you call `run`, `run_sync`, or `run_stream` more than once within a single `capture_run_messages` context, `messages` will represent the messages exchanged during the first call only.
Source code in `pydantic_ai_slim/pydantic_ai/_agent_graph.py`
```
702
703
704
705
706
707
708
709
710
711
712
713
714
715
716
717
718
719
720
721
722
723
724
725
726
727
728
729
730
731
732
733
734
```
| ```
@contextmanager
def capture_run_messages() -> Iterator[list[_messages.ModelMessage]]:
"""Context manager to access the messages used in a [`run`][pydantic_ai.Agent.run], [`run_sync`][pydantic_ai.Agent.run_sync], or [`run_stream`][pydantic_ai.Agent.run_stream] call.
  Useful when a run may raise an exception, see [model errors](../agents.md#model-errors) for more information.
  Examples:
  ```python
  from pydantic_ai import Agent, capture_run_messages
  agent = Agent('test')
  with capture_run_messages() as messages:
    try:
      result = agent.run_sync('foobar')
    except Exception:
      print(messages)
      raise
  ```
  !!! note
    If you call `run`, `run_sync`, or `run_stream` more than once within a single `capture_run_messages` context,
    `messages` will represent the messages exchanged during the first call only.
  """
  try:
    yield _messages_ctx_var.get().messages
  except LookupError:
    messages: list[_messages.ModelMessage] = []
    token = _messages_ctx_var.set(_RunMessages(messages))
    try:
      yield messages
    finally:
      _messages_ctx_var.reset(token)

```
  
---|---
