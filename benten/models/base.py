from typing import List

from ..langserver.lspobjects import Diagnostic, CompletionList, CompletionItem, Range, Position


class Base:
    def __init__(
            self, lines: List[str], ydict: (dict, str), existing_issues: List[Diagnostic]=None):
        self.lines = lines
        self.ydict = ydict
        self.problems: List[Diagnostic] = existing_issues or []

    def completions(self, position: Position, snippets: dict):
        return self._quick_completions(
            position=position,
            snippets=snippets,
            snippet_keys=None)

    def definition(self, position: Position, base_uri: str):
        return None

    def symbols(self):
        return []

    def _quick_completions(self, position: Position, snippets: dict, snippet_keys=None):
        return self._completions_with_range(
            _range=self._range_to_delete_prefix(position),
            snippets=snippets,
            snippet_keys=snippet_keys)

    @staticmethod
    def _completions_with_range(_range: Range, snippets: dict, snippet_keys: List[str]):

        def set_range(_snip: CompletionItem):
            _snip.set_range(_range)
            return _snip

        return CompletionList(
            is_incomplete=False,
            items=[
                set_range(snip) for k, snip in snippets.items()
                if k in snippet_keys
            ]
        )

    def _range_to_delete_prefix(self, position: Position):
        prefix = self.lines[position.line][:position.character]
        try:
            idx = prefix.rindex(" ") + 1
        except ValueError:
            idx = 0
        return Range(
            start=Position(line=position.line, character=idx),
            end=position
        )
